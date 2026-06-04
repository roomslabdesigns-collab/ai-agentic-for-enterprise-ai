# test_ollama.py

import ollama

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "hello"
        }
    ]
)

print(response)