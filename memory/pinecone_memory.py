import os
import uuid
from dotenv import load_dotenv
from openai import AsyncOpenAI
from pinecone import Pinecone

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "ai-content-memory")

if PINECONE_API_KEY:
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX_NAME)
else:
    index = None

embedding_client = AsyncOpenAI()

async def store_memory(text: str, namespace: str = "default", metadata: dict | None = None) -> None:
    """Store text in Pinecone vector DB using OpenAI embeddings."""
    if index is None:
        return
    response = await embedding_client.embeddings.create(
        model="text-embedding-3-small",
        input=[text],
    )
    vector = response.data[0].embedding
    meta = metadata or {}
    meta.update({"text": text})
    upsert_response = index.upsert(vectors=[(str(uuid.uuid4()), vector, meta)], namespace=namespace)
    return upsert_response.upserted_count > 0
