# pip install sentence-transformers
# pip install -U sentence-transformers

import
from sentence_transformers import SentenceTransformer
from chromadb.utils import  embedding_functions

chroma_client = chromadb.persist_directory(path="my_vectordb")

