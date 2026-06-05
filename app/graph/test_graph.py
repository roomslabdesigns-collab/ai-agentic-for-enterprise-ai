from app.graph.workflow import graph

response = graph.invoke(
    {
        "question": "What is my name?"
    }
)

print(response)