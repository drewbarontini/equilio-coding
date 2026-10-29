def create_task(tasks, title):
    tasks.append({"title": title})
    return {"status": 201}
