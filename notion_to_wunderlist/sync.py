from dotenv import load_dotenv
from sys import argv

# from . import wunderlist_tasks
# from . import notion_tasks

import wunderlist_tasks
import notion_tasks

load_dotenv()


def status_is_same(notion_status, wunderlist_complete):
    # notion_status: Not Started, In Progress, Completed
    # wunderlist_complete: True, False
    if wunderlist_complete and notion_status == "Completed":
        return True
    if (not wunderlist_complete) and notion_status != "Completed":
        return True

    return False


def check_task_status(notion_task, w_task_name, wunderlist_task):
    if w_task_name == wunderlist_task['title']:
        if not status_is_same(notion_task.status, wunderlist_task['completed']):
            if not wunderlist_task['completed']:
                return 'update_wunderlist'
            # TODO: figure out how to bi-directionally sync
        return 'nothing'
    return False


def main():
    list_name = ""
    if len(argv) > 1:
        list_name = argv[1]
    else:
        exit("You must provide a Wunderlist list name")

    wunderlist_list = wunderlist_tasks.fetch_list_with_title(list_name)
    wunderlist_tasklist = wunderlist_tasks.get_tasks(list_name)
    notion_tasklist = notion_tasks.get_tasks()

    for n_task in notion_tasklist:
        operation = 'create'
        update_w_task = {}
        w_task_name = "{} (notion)".format(n_task.name)
        for w_task in wunderlist_tasklist:
            task_operation = check_task_status(n_task, w_task_name, w_task)
            if task_operation:
                operation = task_operation
                update_w_task = w_task

        if operation == 'create':
            wunderlist_tasks.create_task(
                wunderlist_list['id'], w_task_name, n_task.status == "Completed")
        elif operation == 'update_wunderlist':
            wunderlist_tasks.update_task(
                list_name, update_w_task, n_task.status == "Completed")
        # elif operation == 'update_notion':
        #     update_notion_status(nt)


if __name__ == '__main__':
    main()
