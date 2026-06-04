from sqlalchemy import (
    Column,
    Integer,
    Text
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    question = Column(Text)

    answer = Column(Text)