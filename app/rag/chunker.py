from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=5000,
        chunk_overlap=500
    )

    chunks = splitter.split_text(text)

    return chunks
