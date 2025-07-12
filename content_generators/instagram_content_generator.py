import os
import sys
# Third-party
from openai import AsyncOpenAI
from dotenv import load_dotenv
# Add the parent directory to the system path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prompts.instagram_content_prompts import instagram_prompt, instagram_system_prompt,instagram_prompt_post_example
from memory.pinecone_memory import retrieve_memory

# Load environment variables from .env file
load_dotenv()
client = AsyncOpenAI()

async def generate_instagram_content(draft: str) -> str:
    examples = await retrieve_memory(draft, namespace="Instagram")
    
    if examples:
        examples_text = ' '.join(examples)
    else:
        examples_text = instagram_prompt_post_example

    user_prompt = f"""
    {instagram_prompt}

    DRAFT: {draft}

    EXAMPLE POST:
    {examples_text}
    """
    # Call the OpenAI responses API asynchronously.
    response = await client.responses.create(
        model="gpt-4o",
        instructions=instagram_system_prompt,
        input=user_prompt,
        temperature=0.7,
        top_p=1,
        max_output_tokens=1024,
        store=True
    )
    return response.output_text


# Example usage for testing:
if __name__ == "__main__":
    draft = "the benefits of remote work"
    response = generate_instagram_content(draft)
    
    



