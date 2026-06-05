from app.graph.workflow import graph

response = graph.invoke(
    {
        "question": "What is natural language processing?"
    }
)

print(response)