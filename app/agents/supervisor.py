from app.agents.sql_agent import (
    answer_database_question
)

from app.rag.rag_pipeline import (
    ask_question
)


def supervisor(question):

    question_lower = question.lower()

    if (
        "how many chats" in question_lower
        or "chat history" in question_lower
        or "database" in question_lower
    ):

        return answer_database_question(
            question
        )

    return ask_question(
        question
    )