from pypdf import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    pdf_path = r"document\thamada ashish final.pdf"

    text = extract_text(pdf_path)

    print(text[:1000])