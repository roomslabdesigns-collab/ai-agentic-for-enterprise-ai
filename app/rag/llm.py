from ollama import Client

client = Client(
    host='http://127.0.0.1:11434'
)

def generate_answer(context, question):

    prompt = f"""
You are an enterprise AI assistant.

Use only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat(
        model='qwen3:4b',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']