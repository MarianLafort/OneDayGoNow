from fastapi import FastAPI, Request
import json
from datetime import datetime

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.json()

    # Zapis do pliku
    with open("webhook.log", "a", encoding="utf-8") as f:
        f.write(f"\n=== {datetime.now()} ===\n")
        f.write(json.dumps(payload, indent=2, ensure_ascii=False))

    print("Webhook received:", payload)
    return {"status": "received"}
