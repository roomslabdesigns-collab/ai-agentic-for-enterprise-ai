from app.database.db import SessionLocal

from app.database.crud import (
    save_memory,
    get_memory
)

db = SessionLocal()

save_memory(
    db,
    "user_name",
    "Ashish"
)

memory = get_memory(
    db,
    "user_name"
)

print(memory.value)