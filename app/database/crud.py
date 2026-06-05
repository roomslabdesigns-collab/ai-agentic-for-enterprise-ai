from app.database.models import (
    ChatHistory,
    Document,
    Memory
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


def save_memory(
    db,
    key,
    value
):

    memory = Memory(
        key=key,
        value=value
    )

    db.add(memory)

    db.commit()

    db.refresh(memory)

    return memory


def get_memory(
    db,
    key
):

    return db.query(
        Memory
    ).filter(
        Memory.key == key
    ).first()