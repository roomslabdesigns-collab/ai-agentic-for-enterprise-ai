import numpy as np

from app.rag.document_manager import load_all_documents
from app.rag.chunker import chunk_text
from app.rag.embedded import create_embeddings, model
from app.rag.vector_store import create_faiss_index, search
from app.rag.llm import generate_answer

# Load all uploaded PDFs
documents = load_all_documents()

# Store chunks from all documents
all_chunks = []

for document in documents:

    chunks = chunk_text(
        document["text"]
    )

    all_chunks.extend(chunks)

print(f"Total Documents Loaded: {len(documents)}")
print(f"Total Chunks Created: {len(all_chunks)}")

# Create embeddings for all chunks
embeddings = create_embeddings(
    all_chunks
)

# Create FAISS index
index = create_faiss_index(
    embeddings
)

def ask_question(question):

    query_embedding = model.encode(
        [question]
    )

    distances, indices = search(
        index,
        np.array(query_embedding),
        k=3
    )

    context = ""

    for idx in indices[0]:

        context += all_chunks[idx]
        context += "\n\n"

    answer = generate_answer(
        context,
        question
    )

    return answer