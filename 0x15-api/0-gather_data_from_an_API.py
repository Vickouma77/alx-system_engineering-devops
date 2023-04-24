#!/usr/bin/python3
"""returns information about TODO list progress"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Request failed with status code {response.status_code}")
        sys.exit(1)

    tasks = response.json()
    num_total_task = len(tasks)
    completed = len([task for task in tasks if task["completed"]])

    employee_name = tasks[0]["name"]
    print(f"Employee {employee_name} is done with tasks"
          f"({num_completed_tasks}/{num_total_tasks}):")

    for task in tasks:
        if tasks["completed"]:
            print(f"\t{task['title']}")
