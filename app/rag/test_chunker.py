from pdf_loader import extract_text
from chunker import chunk_text

text = extract_text("document/thamada ashish final.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])

for i in range(min(3, len(chunks))):
    print(f"\nChunk {i+1}\n")
    print(chunks[i])
    print("-" * 50)