import numpy as np

from pdf_loader import extract_text
from chunker import chunk_text
from embedded import create_embeddings, model
from vector_store import create_faiss_index, search
from llm import generate_answer


text = extract_text(
    "document/thamada ashish final.pdf"
)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

question = input("Ask Question: ")

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
    context += chunks[idx]
    context += "\n\n"

answer = generate_answer(
    context,
    question
)

print("\nAnswer:\n")

print(answer)