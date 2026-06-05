from langgraph.graph import StateGraph
from langgraph.graph import END

from app.graph.state import AgentState

from app.agents.sql_agent import (
    answer_database_question
)

from app.rag.rag_pipeline import (
    ask_question
)


# SQL NODE
def sql_node(state):

    question = state["question"]

    answer = answer_database_question(
        question
    )

    return {
        "answer": answer
    }


# RAG NODE
def rag_node(state):

    question = state["question"]

    answer = ask_question(
        question
    )

    return {
        "answer": answer
    }


# ROUTER NODE
def route_question(state):

    question = state["question"].lower()

    sql_keywords = [
        "how many chats",
        "latest question",
        "show chats",
        "how many documents",
        "show documents",
        "latest document"
    ]

    if any(
        keyword in question
        for keyword in sql_keywords
    ):
        return "sql"

    return "rag"


# BUILD GRAPH

workflow = StateGraph(
    AgentState
)

workflow.add_node(
    "sql",
    sql_node
)

workflow.add_node(
    "rag",
    rag_node
)

workflow.set_conditional_entry_point(
    route_question,
    {
        "sql": "sql",
        "rag": "rag"
    }
)

workflow.add_edge(
    "sql",
    END
)

workflow.add_edge(
    "rag",
    END
)

graph = workflow.compile()