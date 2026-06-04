from app.database.models import (
    ChatHistory,
    Document
)


def save_chat(
    db,
    question,
    answer
):

    chat = ChatHistory(
        question=question,
        answer=answer
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat


def get_chat_history(db):

    return db.query(
        ChatHistory
    ).all()


def save_document(
    db,
    filename,
    chunk_count
):

    document = Document(
        filename=filename,
        chunk_count=chunk_count
    )

    db.add(document)

    db.commit()

    db.refresh(document)

    return document