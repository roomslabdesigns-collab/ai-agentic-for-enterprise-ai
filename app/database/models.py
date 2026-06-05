from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    DateTime
)

from sqlalchemy.orm import declarative_base

from datetime import datetime

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


class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String
    )

    chunk_count = Column(
        Integer
    )

    upload_time = Column(
        DateTime,
        default=datetime.utcnow
    )


class Memory(Base):

    __tablename__ = "memory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    key = Column(
        String
    )

    value = Column(
        Text
    )