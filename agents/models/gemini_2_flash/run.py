# requires Gemini API KEY and ENdpoint URL
## GEMINI_API_KEY="xxxxx"
## GEMINI_API_ENDPOINT="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
## Create .env file at root of the project
from google import genai
import os

def Run(query):
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
    response = client.models.generate_content(model="gemini-2.0-flash", contents=query)
    return response.text