from fastapi import FastAPI, Request, Header, HTTPException
from app.handlers import issues, pull_requests, ping
import hmac
import hashlib
import os

app = FastAPI()

GITHUB_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")

@app.post("/webhook")
async def webhook(request: Request, x_hub_signature_256: str = Header(None), x_github_event: str = Header(None)):
    body = await request.body()

    # Weryfikacja podpisu webhooka
    if GITHUB_SECRET:
        signature = 'sha256=' + hmac.new(GITHUB_SECRET.encode(), body, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, x_hub_signature_256):
            raise HTTPException(status_code=403, detail="Invalid signature")

    payload = await request.json()

    # Przekierowanie do handlera
    if x_github_event == "ping":
        return ping.handle(payload)
    elif x_github_event == "issues":
        return await issues.handle(payload)
    elif x_github_event == "pull_request":
        return await pull_requests.handle(payload)

    return {"msg": "Unhandled event"}
