import os
import sys
# Third-party
from openai import AsyncOpenAI
from dotenv import load_dotenv
# Add the parent directory to the system path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompts.blog_content_prompts import tech_blog_prompt, tech_blog_system_prompt

# Load environment variables from .env file
load_dotenv()
client = AsyncOpenAI()

async def generate_blog_content(draft: str) -> str:
    user_prompt = f"""
    {tech_blog_prompt}

    DRAFT: {draft}
    """
    # Call the OpenAI responses API asynchronously.
    response = await client.responses.create(
        model="gpt-4o",
        instructions=tech_blog_system_prompt,
        input=user_prompt,
        temperature=0.7,
        top_p=1,
        max_output_tokens=4000,
        store=True
    )
    return response.output_text


# Example usage for testing:
if __name__ == "__main__":
    draft = "the benefits of remote work"
    response = generate_blog_content(draft)
    
    



