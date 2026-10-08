import argparse
import csv
import sys


TASKS = [
    {"owner": "alex", "title": "Plan review", "due": "2026-10-12", "completed": False},
    {"owner": "alex", "title": "Send notes", "due": "2026-10-07", "completed": True},
    {"owner": "sam", "title": "Private draft", "due": "2026-10-15", "completed": False},
]


def tasks_for(owner):
    return [task for task in TASKS if task["owner"] == owner]


def export_tasks(owner, destination):
    writer = csv.writer(destination)
    writer.writerow(["title"])
    writer.writerows([task["title"]] for task in tasks_for(owner))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["list", "export"])
    parser.add_argument("--owner", default="alex")
    args = parser.parse_args()
    if args.action == "list":
        for task in tasks_for(args.owner):
            print(task)
    else:
        export_tasks(args.owner, sys.stdout)
