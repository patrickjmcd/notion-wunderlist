import os
from dotenv import load_dotenv
from notion.client import NotionClient

load_dotenv()


def check_task(task, user):
    """Checks to see if the task is assigned to the user."""
    if user in task.assign:
        return True

    elif task.assign == []:
        print("Unassigned Task: {}".format(task.name))


def update_status(wunderlist_task):
    """Updates a notion task."""
    print("Updating task in Notion: {}".format(wunderlist_task['title']))

    all_tasks = _get_all_notion_tasks()
    for t in all_tasks:
        if t.name == wunderlist_task['title']:
            if wunderlist_task['completed']:
                t.status = "Completed"
            else:
                t.status = "In Progress"


def _get_all_notion_tasks():
    """Fetch all notion tasks."""
    NOTION_TOKEN = os.environ['NOTION_TOKEN']
    notion_task_lists = os.environ['NOTION_TASK_LISTS'].split(",")
    tasks = []
    client = NotionClient(token_v2=NOTION_TOKEN)

    for url in notion_task_lists:
        cv = client.get_collection_view(url)
        for t in cv.collection.get_rows():
            tasks.append(t)
    return tasks


def get_tasks():
    NOTION_TOKEN = os.environ['NOTION_TOKEN']
    client = NotionClient(token_v2=NOTION_TOKEN)

    all_tasks = _get_all_notion_tasks()
    tasks = []
    for t in all_tasks:
        if check_task(t, client.current_user):
            tasks.append(t)
    return tasks


if __name__ == '__main__':
    for t in get_tasks():
        print(t)
