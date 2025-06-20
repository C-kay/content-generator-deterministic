import os
import sys
# Third-party
from openai import AsyncOpenAI
from dotenv import load_dotenv
# Add the parent directory to the system path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompts.linkedin_content_prompts import linkedin_system_prompt, linkedin_prompt
from memory.pinecone_memory import store_memory

# Load environment variables from .env file
load_dotenv()
client = AsyncOpenAI()

async def generate_linkedin_content(draft: str) -> str:
    user_prompt = f"""
    {linkedin_prompt}

    DRAFT: {draft}
    """
    # Call the OpenAI responses API asynchronously.
    response = await client.responses.create(
        model="gpt-4o",
        instructions=linkedin_system_prompt,
        input=user_prompt,
        temperature=0.7,
        top_p=1,
        max_output_tokens=2000,
        store=True
    )
    await store_memory(response.output_text, namespace="linkedin", metadata={"draft": draft})
    return response.output_text


# Example usage for testing:
if __name__ == "__main__":
    draft = "the benefits of remote work"
    response = generate_linkedin_content(draft)
    
    



