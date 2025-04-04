import os
import sys
from dotenv import load_dotenv


# Add the parent directory to the system path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content_generators.instagram_content_generator import generate_instagram_content
from content_generators.linkedin_content_generator import generate_linkedin_content
from content_generators.blog_content_generator import generate_blog_content

# Load environment variables from .env file
load_dotenv()

content_generators = {
    "Instagram": generate_instagram_content,
    "LinkedIn": generate_linkedin_content,
    "Blog Post": generate_blog_content
}