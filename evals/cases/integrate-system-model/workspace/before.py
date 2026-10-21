def update_task(tasks, events, task_id, title, notify):
    tasks[task_id] = title
    events.append({"task_id": task_id, "title": title})
    return {"ok": True}
