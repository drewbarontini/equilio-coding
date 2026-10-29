def create_task(tasks, title):
    if not title.strip():
        return {"status": 422, "error": "Title required"}
    tasks.append({"title": title})
    return {"status": 201}
