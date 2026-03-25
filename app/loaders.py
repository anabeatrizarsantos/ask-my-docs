"""
loaders.py

Purpose:
    Load raw knowledge-base files from the data/raw directory and convert them
    into a unified list of LangChain Document objects.

What this module receives:
    - A directory path containing files such as .txt, .pdf, and .docx

What this module returns:
    - A list[Document] ready for splitting, embedding, and indexing

Why this module exists:
    In a RAG pipeline, documents can come from different file formats.
    This module centralizes the loading logic so the rest of the pipeline
    can work with a single consistent structure.

Supported formats:
    - .txt
    - .pdf
    - .docx
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader


SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}


def load_documents(data_dir: str = "data/raw") -> List[Document]:
    """
    Load all supported documents from a directory.

    Args:
        data_dir (str):
            Path to the folder containing the raw documents.

    Returns:
        List[Document]:
            A flat list of LangChain Document objects.

    Raises:
        FileNotFoundError:
            If the provided folder does not exist.
        ValueError:
            If no supported files are found.
    """
    base_path = Path(data_dir)

    if not base_path.exists():
        raise FileNotFoundError(f"Directory not found: {data_dir}")

    documents: List[Document] = []

    # Iterate over all files inside the folder
    for file_path in base_path.iterdir():
        # Skip directories and unsupported file types
        if not file_path.is_file() or file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        loaded_docs = _load_single_file(file_path)
        documents.extend(loaded_docs)

    if not documents:
        raise ValueError(f"No supported documents found in: {data_dir}")

    return documents


def _load_single_file(file_path: Path) -> List[Document]:
    """
    Load one file and return its documents.

    Args:
        file_path (Path):
            Path of the file to load.

    Returns:
        List[Document]:
            Loaded documents from that file.

    Notes:
        - PDF files may return multiple Document objects (often one per page).
        - TXT and DOCX usually return one Document object per file.
    """
    suffix = file_path.suffix.lower()

    if suffix == ".txt":
        loader = TextLoader(str(file_path), encoding="utf-8")
    elif suffix == ".pdf":
        loader = PyPDFLoader(str(file_path))
    elif suffix == ".docx":
        loader = Docx2txtLoader(str(file_path))
    else:
        raise ValueError(f"Unsupported file type: {file_path.name}")

    documents = loader.load()

    # Add standard metadata so later steps can track the source file
    for doc in documents:
        doc.metadata["source_file"] = file_path.name

    return documents