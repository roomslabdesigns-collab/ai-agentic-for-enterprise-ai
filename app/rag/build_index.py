from app.rag.document_manager import load_all_documents
from app.rag.chunker import chunk_text
from app.rag.embedded import create_embeddings
from app.rag.vector_store import (
    create_faiss_index,
    save_index,
    save_chunks
)

documents = load_all_documents()

all_chunks = []

for document in documents:

    chunks = chunk_text(
        document["text"]
    )

    all_chunks.extend(chunks)

embeddings = create_embeddings(
    all_chunks
)

index = create_faiss_index(
    embeddings
)

save_index(
    index,
    "storage/faiss_index.bin"
)

save_chunks(
    all_chunks,
    "storage/chunks.pkl"
)

print("Index Saved Successfully")
print(f"Chunks: {len(all_chunks)}")