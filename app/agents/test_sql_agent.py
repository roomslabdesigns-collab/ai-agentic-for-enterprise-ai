from app.agents.sql_agent import (
    answer_database_question
)

response = answer_database_question(
    "How many chats are stored?"
)

print(response)