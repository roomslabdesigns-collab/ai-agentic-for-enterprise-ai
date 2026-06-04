import numpy as np

from app.rag.embedded import model
from app.rag.vector_store import (
    load_index,
    load_chunks,
    search
)
from app.rag.llm import generate_answer

index = load_index(
    "storage/faiss_index.bin"
)

all_chunks = load_chunks(
    "storage/chunks.pkl"
)

print("FAISS Index Loaded")
print(f"Total Chunks: {len(all_chunks)}")


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