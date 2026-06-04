from sqlalchemy import text

from app.database.db import engine


def answer_database_question(question):

    question = question.lower()

    with engine.connect() as conn:

        # Chat Analytics

        if "how many chats" in question:

            result = conn.execute(
                text(
                    "SELECT COUNT(*) FROM chat_history"
                )
            )

            count = result.scalar()

            return f"There are {count} chats stored in the database."

        elif "latest question" in question:

            result = conn.execute(
                text(
                    """
                    SELECT question
                    FROM chat_history
                    ORDER BY id DESC
                    LIMIT 1
                    """
                )
            )

            row = result.fetchone()

            if row:
                return f"Latest question: {row[0]}"

        elif "show chats" in question:

            result = conn.execute(
                text(
                    """
                    SELECT id, question
                    FROM chat_history
                    ORDER BY id DESC
                    LIMIT 5
                    """
                )
            )

            rows = result.fetchall()

            response = "Recent Chats:\n\n"

            for row in rows:

                response += (
                    f"{row[0]}. {row[1]}\n"
                )

            return response

        # Document Analytics

        elif "how many documents" in question:

            result = conn.execute(
                text(
                    "SELECT COUNT(*) FROM documents"
                )
            )

            count = result.scalar()

            return f"There are {count} documents uploaded."

        elif "show documents" in question:

            result = conn.execute(
                text(
                    """
                    SELECT filename
                    FROM documents
                    ORDER BY id DESC
                    """
                )
            )

            rows = result.fetchall()

            response = "Uploaded Documents:\n\n"

            for row in rows:

                response += (
                    f"- {row[0]}\n"
                )

            return response

        elif "latest document" in question:

            result = conn.execute(
                text(
                    """
                    SELECT filename
                    FROM documents
                    ORDER BY id DESC
                    LIMIT 1
                    """
                )
            )

            row = result.fetchone()

            if row:
                return f"Latest uploaded document: {row[0]}"

    return None