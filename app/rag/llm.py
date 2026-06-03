import ollama


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

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]