import numpy as np

from pdf_loader import extract_text
from chunker import chunk_text
from embedded import create_embeddings, model
from vector_store import create_faiss_index, search


text = extract_text(
    "document/thamada ashish final.pdf"
)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = create_faiss_index(embeddings)

query = "Brain tumor detection methodology"

query_embedding = model.encode(
    [query]
)

distances, indices = search(
    index,
    np.array(query_embedding),
    k=3
)

print("Top Matching Chunks:\n")

for idx in indices[0]:

    print("\n" + "=" * 60)

    print(chunks[idx])