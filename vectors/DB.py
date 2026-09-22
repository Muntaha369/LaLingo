from dotenv import load_dotenv
import chromadb
from rich import print
from langchain_mistralai import MistralAIEmbeddings

load_dotenv()

client = chromadb.PersistentClient(path="./chroma_db")

embedder = MistralAIEmbeddings(model="mistral-embed")

# No embedding_function passed — collection just stores vectors you give it
collection = client.get_or_create_collection(name="my_docs")

documents = [
    "Python is a popular programming language for machine learning.",
    "Chroma is an open-source vector database.",
    "Transformers revolutionized NLP with the attention mechanism.",
    "Cats are small domesticated carnivorous mammals."
]
metadatas = [
    {"topic": "programming"},
    {"topic": "database"},
    {"topic": "ml"},
    {"topic": "animals"}
]
ids = ["doc1", "doc2", "doc3", "doc4"]

# Embed manually using Mistral's own method
doc_embeddings = embedder.embed_documents(documents)

collection.add(
    documents=documents,
    embeddings=doc_embeddings, #type:ignore
    metadatas=metadatas, #type:ignore
    ids=ids
)

# For queries, Mistral distinguishes query vs document embeddings — use embed_query
query = "What is used for storing embeddings?"
query_embedding = embedder.embed_query(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

for doc, dist, meta in zip(
    results["documents"][0], #type:ignore
    results["distances"][0], #type:ignore
    results["metadatas"][0] #type:ignore
):
    print(f"{dist:.4f} | {meta['topic']} | {doc}")