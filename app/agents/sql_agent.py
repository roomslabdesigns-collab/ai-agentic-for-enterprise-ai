from sqlalchemy import text

from app.database.db import engine


def answer_database_question(question):

    question = question.lower()

    if "how many chats" in question:

        with engine.connect() as conn:

            result = conn.execute(
                text(
                    "SELECT COUNT(*) FROM chat_history"
                )
            )

            count = result.scalar()

        return f"There are {count} chats stored in the database."

    return None