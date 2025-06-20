# AI Social Media Manager

**AI Social Media Manager** is an autonomous, agent-driven solution that creates, schedules, and optimizes social media content for influencers and businesses. Built using OpenAI's Agents SDK and leveraging the new Responses API, this project streamlines content creation, posting, and performance optimization—all with minimal human intervention.

## Key Features
- **Content Generation:** Automatically generate creative social media posts (captions, hashtags, image prompts) using GPT-4o.
- **Scheduling:** Integrate with social media APIs to post content at optimal times.
- **Optimization:** Analyze engagement data and adjust strategies for improved performance.
- **Agent Orchestration:** Use dedicated agents for content generation, scheduling, and optimization, coordinated through a central handoff agent.
- **Built-in Tools:** Utilize web search for trending topics and image generation (via DALL-E integration) to enhance posts.
- **Long-Term Memory:** Generated content is stored in a Pinecone vector database for later retrieval and analysis.

## Project Structure

```
ai-social-media-manager/
├── README.md                  # Project overview and setup instructions
├── requirements.txt           # Python dependencies
├── setup.py                   # Packaging script
├── .env                       # Environment variables (API keys, secrets, etc.)
├── config/
│   └── config.yaml            # Configuration settings (social media API endpoints, scheduling preferences)
├── content_generators/
│   ├── __init__.py
│   ├── linkedin_content_generator.py  # Generates LinkedIn content
│   ├── instagram_content_generator.py # Generates Instagram content
│   ├── blog_content_generator.py      # Generates blog content
├── scripts/
│   ├── run_generators.py      # Script to run content generation tasks
├── api/
│   ├── __init__.py
│   └── api.py                 # FastAPI application for exposing endpoints
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-social-media-manager.git
   cd ai-social-media-manager
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate        # On Unix/MacOS
   env\Scripts\activate           # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   SOCIAL_MEDIA_API_KEY=your_social_media_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
   PINECONE_INDEX_NAME=ai-content-memory
   ```

## Usage

### Run the Workflow
Run the complete agent workflow with:
```bash
python scripts/run_agent.py
```
This script initializes the various agents (content generation, scheduling, and optimization), coordinates their interaction, and executes the workflow to generate, schedule, and optimize a social media post.

### Run Content Generators
To generate content for specific platforms, use:
```bash
python scripts/run_generators.py
```

### API Endpoints
Start the FastAPI server:
```bash
uvicorn api.api:app --host 0.0.0.0 --port 8000
```
Access the API documentation at `http://localhost:8000/docs`.

## Configuration

Customize settings in `config/config.yaml` to adjust:
- Social media API endpoints
- Scheduling preferences
- Other project-specific parameters

## Testing

Run unit tests to ensure proper functionality:
```bash
pytest tests/
```

## Deployment

### Render.com
To deploy the application on Render, use the following start command:
```bash
uvicorn api.api:app --host 0.0.0.0 --port 8000
```

### Docker
If you want to containerize the application, create a `Dockerfile` and build the image:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000"]
```
Build and run the Docker container:
```bash
docker build -t ai-social-media-manager .
docker run -p 8000:8000 ai-social-media-manager
```

## Contributing

Contributions are welcome! Please fork the repository, create your feature branch, and submit a pull request. Refer to [CONTRIBUTING.md](CONTRIBUTING.md) for details on our contribution process.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or support, please contact [ckobieyisi@gmail.com](mailto:ckobieyisi@gmail.com).

---

**AI Social Media Manager** leverages cutting-edge AI technology to revolutionize how content is managed on social media—making it more creative, efficient, and effective.