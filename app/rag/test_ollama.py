from ollama import Client

client = Client(
    host="http://127.0.0.1:11434"
)

response = client.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(
    response["message"]["content"]
)