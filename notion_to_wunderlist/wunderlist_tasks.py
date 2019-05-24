import wunderpy2
from dotenv import load_dotenv
from sys import argv
from os import getenv

load_dotenv()


def get_wunderlist_client():
    ACCESS_TOKEN = getenv('WUNDERLIST_ACCESS_TOKEN')
    CLIENT_ID = getenv('WUNDERLIST_CLIENT_ID')
    api = wunderpy2.WunderApi()
    client = api.get_client(ACCESS_TOKEN, CLIENT_ID)
    return client


def fetch_list_with_title(title, client=None):
    if not client:
        client = get_wunderlist_client()
    lists = client.get_lists()
    return list(filter(lambda l: l['title'] == title, lists))[0]


def get_tasks(list_name):
    client = get_wunderlist_client()

    this_list = fetch_list_with_title(list_name, client)
    incomplete_tasks = client.get_tasks(this_list['id'])
    complete_tasks = client.get_tasks(this_list['id'], completed=True)
    all_tasks = incomplete_tasks + complete_tasks
    return all_tasks


def create_task(list_name, title, completed):
    client = get_wunderlist_client()
    print("Creating Wunderlist task {}".format(title))
    return client.create_task(list_name, title, completed=completed)


def update_task(list_name, w_task, status):
    client = get_wunderlist_client()
    print("Updating Wunderlist task {} to be completed={}".format(
        w_task['title'], status))
    return client.update_task(w_task['id'], w_task['revision'], completed=status)


def main(list_name):
    print(get_tasks(list_name))


if __name__ == '__main__':

    if len(argv) > 1:
        main(argv[1])
    else:
        exit("You must provide a list name")
