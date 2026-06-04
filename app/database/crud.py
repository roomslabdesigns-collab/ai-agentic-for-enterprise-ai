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
    
def get_chat_history(db):

    return db.query(
        ChatHistory
    ).all()

    return chat
