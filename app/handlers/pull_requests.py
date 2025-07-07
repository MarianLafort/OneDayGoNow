async def handle(payload):
    action = payload.get("action")
    pr = payload.get("pull_request", {})
    title = pr.get("title")
    user = pr.get("user", {}).get("login")

    if action == "opened":
        print(f"Nowy pull request od @{user}: {title}")

    return {"msg": f"Przetworzono PR: {action}"}
