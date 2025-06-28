import os
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from content_generators.content_generator import content_generators
from content_generators.context import WorkflowResponse
from memory.pinecone_memory import store_memory

# Load environment variables
load_dotenv()

# Define the expected request payload
class WorkflowRequest(BaseModel):
    topic_draft: str
    platforms: list[str]

#
class SaveContentRequest(BaseModel):
    text: str
    namespace: str = "default"
    metadata: dict | None = None

# Initialize FastAPI app
app = FastAPI()

# Define available platforms
AVAILABLE_PLATFORMS = {
    "LinkedIn": {"id": 1, "name": "LinkedIn"},
    "Instagram": {"id": 2, "name": "Instagram"},
    "Twitter": {"id": 3, "name": "Twitter"},
    "Facebook": {"id": 4, "name": "Facebook"},
    "TikTok": {"id": 5, "name": "TikTok"},
    "Blog Post": {"id": 6, "name": "Blog Post"},
}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://content-creator-ui.onrender.com"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

def create_task(platform: str, topic_draft: str):
    if platform not in content_generators:
        raise ValueError(f"Unsupported platform: {platform}")
    return asyncio.create_task(content_generators[platform](topic_draft))

@app.post("/execute_workflow")
async def execute_workflow_endpoint(request: WorkflowRequest):

    try:
        # Create tasks for the requested platforms
        tasks = [create_task(platform, request.topic_draft) for platform in request.platforms]
        
        # Run tasks concurrently
        results = await asyncio.gather(*tasks)

        # Build the response
        response_content = [
            {
                "id": AVAILABLE_PLATFORMS[platform]["id"],
                "name": platform,
                "content": content,
            }
            for platform, content in zip(request.platforms, results)
        ]

        return WorkflowResponse(content=response_content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing workflow: {str(e)}")

@app.post("/execute_single_platform")
async def execute_single_platform(request: WorkflowRequest):
    try:
        # Validate platform
        if len(request.platforms) != 1:
            raise HTTPException(status_code=400, detail="Exactly one platform must be specified.")
        
        platform = request.platforms[0]
        if platform not in AVAILABLE_PLATFORMS:
            raise HTTPException(status_code=400, detail=f"Unsupported platform: {platform}")

        # Create and run the task for the specified platform with the provided topic draft
        task = create_task(platform, request.topic_draft)
        result = await task

        # Build the response
        response_content = {
            "id": AVAILABLE_PLATFORMS[platform]["id"],
            "name": platform,
            "content": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing platform task: {str(e)}")

    return response_content

@app.post("/save_liked_content")
async def save_liked_content(request: SaveContentRequest):
    try:
        isSaved = await store_memory(request.text, namespace=request.namespace, metadata=request.metadata)
        if isSaved:
            return {"status": "success", "message": "Content saved to memory."}
        else:
            return {"status": "error", "message": "Failed to save content to memory."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving content: {str(e)}")

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)