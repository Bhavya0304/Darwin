# requires GROQ API KEY
## GROQ_API="xxxxx"
## Create .env file at root of the project

from groq import Groq
import os

def Run(query):
    client = Groq(api_key=os.getenv("GROQ_API"))
    chat_completion = client.chat.completions.create(messages=[{"role": "user","content": query,}],model="llama-3.3-70b-versatile",)
    return chat_completion.choices[0].message.content