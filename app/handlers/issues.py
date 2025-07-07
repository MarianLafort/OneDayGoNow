async def handle(payload):
    action = payload.get("action")
    issue = payload.get("issue", {})
    title = issue.get("title")
    user = issue.get("user", {}).get("login")

    if action == "opened":
        print(f"Nowe zgłoszenie od @{user}: {title}")

    return {"msg": f"Przetworzono zgłoszenie: {action}"}
