import os
import sys
from dotenv import load_dotenv
import asyncio

# Append the project root directory to sys.path so that the 'agents' package is found.
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from content_generators.instagram_content_generator import generate_instagram_content
from content_generators.linkedin_content_generator import generate_linkedin_content
from content_generators.blog_content_generator import generate_blog_content

load_dotenv()

async def main():
    # Define a sample topic for which to generate a social media post
    draft = "the benefits of remote work"

    try:
        # Run LinkedIn and Instagram content generation concurrently.
        linkedin_task = asyncio.create_task(generate_linkedin_content(draft))
        instagram_task = asyncio.create_task(generate_instagram_content(draft))
        blog_task = asyncio.create_task(generate_blog_content(draft))
        
        linkedin_content, instagram_content, blog_content = await asyncio.gather(linkedin_task, instagram_task, blog_task)

        print("LinkedIn Content:")
        print(linkedin_content)
        print("\nInstagram Content:")
        print(instagram_content)
        print("\nBlogContent:")
        print(blog_content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
