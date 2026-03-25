"""
splitter.py

Purpose:
    Split loaded LangChain Document objects into smaller chunks that are
    easier for embeddings models and retrieval systems to handle.

What this module receives:
    - A list of LangChain Document objects

What this module returns:
    - A list[Document] with smaller chunked documents

Why this module exists:
    In RAG, large documents are usually not sent directly to the vector store.
    They are first broken into smaller overlapping pieces ("chunks") so that:
    - retrieval becomes more precise
    - embeddings capture more focused meaning
    - context windows are used more efficiently

Main strategy used here:
    - RecursiveCharacterTextSplitter

Important parameters:
    - chunk_size: maximum approximate size of each chunk
    - chunk_overlap: repeated text between consecutive chunks to preserve context
"""

from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(
    documents: List[Document],
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> List[Document]:
    """
    Split documents into smaller overlapping chunks.

    Args:
        documents (List[Document]):
            Original loaded documents.
        chunk_size (int):
            Approximate maximum size of each chunk.
        chunk_overlap (int):
            Number of overlapping characters between chunks.

    Returns:
        List[Document]:
            Chunked documents ready for embeddings and indexing.

    Raises:
        ValueError:
            If the input document list is empty.
    """
    if not documents:
        raise ValueError("The document list is empty. Nothing to split.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunked_documents = splitter.split_documents(documents)

    return chunked_documents