from app.database.db import SessionLocal

from app.database.crud import (
    save_memory,
    get_memory
)


def memory_handler(question):

    db = SessionLocal()

    question_lower = question.lower()

    if "my name is" in question_lower:

        name = question.split(
            "My name is",
            1
        )[1].strip()

        save_memory(
            db,
            "user_name",
            name
        )

        return f"I'll remember that your name is {name}."

    elif "what is my name" in question_lower:

        memory = get_memory(
            db,
            "user_name"
        )

        if memory:
            return f"Your name is {memory.value}."

        return "I don't know your name yet."

    return None