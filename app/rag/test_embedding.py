from pdf_loader import extract_text
from chunker import chunk_text
from embedded import create_embeddings

text = extract_text(
    "document/thamada ashish final.pdf"
)

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))

print("Number of embeddings:", len(embeddings))

print("\nEmbedding Shape:")
print(embeddings.shape)

print("\nFirst 10 values of first embedding:")
print(embeddings[0][:10])