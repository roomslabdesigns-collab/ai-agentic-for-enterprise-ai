import numpy as np

from app.rag.pdf_loader import extract_text
from app.rag.chunker import chunk_text
from app.rag.embedded import create_embeddings, model
from app.rag.vector_store import create_faiss_index, search
from app.rag.llm import generate_answer

text = extract_text(
    "document/thamada ashish final.pdf"
)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

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
        context += chunks[idx]
        context += "\n\n"

    answer = generate_answer(
        context,
        question
    )

    return answer