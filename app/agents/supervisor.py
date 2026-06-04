from app.agents.sql_agent import (
    answer_database_question
)

from app.rag.rag_pipeline import (
    ask_question
)


def supervisor(question):

    question_lower = question.lower()

    if any(
    keyword in question_lower
    for keyword in [
        "how many chats",
        "latest question",
        "show chats",
        "chat history",
        "database"
        ]
    ):  

        return answer_database_question(
            question
        )

    return ask_question(
        question
    )