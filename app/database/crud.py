from app.database.models import ChatHistory


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