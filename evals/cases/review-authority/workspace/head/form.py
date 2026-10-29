from api import create_task


def submit(tasks, title):
    if not title.strip():
        return {"status": 422, "field": "title", "error": "Title required"}
    return create_task(tasks, title)
