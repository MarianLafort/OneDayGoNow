from fastapi import FastAPI, Request
import json
from datetime import datetime

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.json()
    print("Webhook received:", payload)

    # Zapisz do webhook.log
    with open("webhook.log", "a") as f:
        f.write(f"[{datetime.now()}] {json.dumps(payload)}\n")

    return {"status": "received"}
