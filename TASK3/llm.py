import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-1.5-flash"

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

def analyze_article(text):

    prompt = f"""
You are a news processing engine.

From the article below, extract:

1. category → one of: Sports, Technology, Politics, India
2. sentiment → one of: Positive, Negative, Neutral
3. summary → exactly 5 lines

Return ONLY valid JSON in this format:

{{
  "category": "...",
  "sentiment": "...",
  "summary": "..."
}}

Article:
{text}
"""

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "application/json"
        }
    }

    response = requests.post(URL, json=payload)
    response.raise_for_status()

    raw = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    return json.loads(raw)
