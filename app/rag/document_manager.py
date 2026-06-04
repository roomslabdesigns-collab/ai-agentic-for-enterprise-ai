import os

from app.rag.pdf_loader import extract_text


def load_all_documents():

    documents = []

    upload_dir = "uploads"

    for file in os.listdir(upload_dir):

        if file.endswith(".pdf"):

            path = os.path.join(
                upload_dir,
                file
            )

            text = extract_text(path)

            documents.append(
                {
                    "filename": file,
                    "text": text
                }
            )

    return documents