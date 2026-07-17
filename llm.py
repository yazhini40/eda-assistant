import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_llm_insights(summary: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a data analyst. Given a statistical summary of a dataset, provide clear and concise insights in plain English."
            },
            {
                "role": "user",
                "content": f"Here is the dataset summary:\n{summary}\n\nProvide key insights."
            }
        ]
    )
    return response.choices[0].message.content