"""
embeddings.py

Purpose:
    Create and return the embeddings model used to transform text chunks
    into vectors for semantic search.

What this module receives:
    - Configuration values from environment variables (.env)

What this module returns:
    - An embeddings client compatible with LangChain vector stores

Why this module exists:
    In a RAG pipeline, the embeddings model is responsible for converting
    text into numeric vectors. These vectors are what allow the system to
    compare semantic similarity between a user question and stored chunks.

Current provider:
    - Azure OpenAI

Expected environment variables:
    - AZURE_OPENAI_API_KEY
    - AZURE_OPENAI_ENDPOINT
    - AZURE_OPENAI_API_VERSION
    - AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT
"""

import os

from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings


# Load variables from the .env file into the environment
load_dotenv()


def get_embeddings_model() -> AzureOpenAIEmbeddings:
    """
    Create and return the Azure OpenAI embeddings model.

    Returns:
        AzureOpenAIEmbeddings:
            Configured embeddings client ready to be used by a vector store.

    Raises:
        ValueError:
            If one or more required environment variables are missing.
    """
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    deployment = os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT")

    # Validate required configuration before creating the client
    missing_vars = [
        var_name
        for var_name, value in {
            "AZURE_OPENAI_API_KEY": api_key,
            "AZURE_OPENAI_ENDPOINT": azure_endpoint,
            "AZURE_OPENAI_API_VERSION": api_version,
            "AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT": deployment,
        }.items()
        if not value
    ]

    if missing_vars:
        missing = ", ".join(missing_vars)
        raise ValueError(f"Missing required environment variables: {missing}")

    return AzureOpenAIEmbeddings(
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
        azure_deployment=deployment,
    )