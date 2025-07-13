from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    payload = await request.json()

    # --- log do terminala ---
    print("\n=== Webhook received ===")
    print(payload)

    # --- log do pliku ---
    with open("webhook.log", "a", encoding="utf-8") as f:
        f.write("\n=== Webhook received ===\n")
        f.write(str(payload) + "\n")

    return {"status": "received"}
