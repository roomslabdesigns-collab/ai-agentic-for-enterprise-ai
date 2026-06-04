from app.rag.document_manager import (
    load_all_documents
)

documents = load_all_documents()

print(
    f"Total Documents: {len(documents)}"
)

for doc in documents:

    print("\n")
    print(doc["filename"])