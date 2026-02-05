from fastapi import FastAPI
from llm import analyze_article
from db import save_article

app = FastAPI()

@app.post("/process")
def process_article(article: dict):

    text = article["content"]

    ai_result = analyze_article(text)

    processed = {
        **article,
        "category": ai_result["category"],
        "sentiment": ai_result["sentiment"],
        "summary": ai_result["summary"]
    }

    save_article(processed)

    return processed
