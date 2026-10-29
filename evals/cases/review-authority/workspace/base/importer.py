from api import create_task


def import_rows(tasks, rows):
    return [create_task(tasks, row["title"]) for row in rows]
