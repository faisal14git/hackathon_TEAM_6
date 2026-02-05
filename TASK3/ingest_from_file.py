import json
import requests

PROCESSOR_URL = "http://localhost:8001/process"


FILE_PATH = "redis_export.json"

def main():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    articles = data.get("news_pipeline", [])

    print(f"Found {len(articles)} articles")

    for item in articles:
        try:
            article = json.loads(item)

            payload = {
                "title": article.get("title"),
                "content": article.get("full_text"),
                "source": article.get("source"),
                "url": article.get("url"),
                "published_at": article.get("published_at")
            }

            r = requests.post(PROCESSOR_URL, json=payload)

            if r.status_code == 200:
                print("Inserted:", payload["title"])
            else:
                print("Failed:", payload["title"], r.text)

        except Exception as e:
            print("Error parsing article:", e)

if __name__ == "__main__":
    main()
