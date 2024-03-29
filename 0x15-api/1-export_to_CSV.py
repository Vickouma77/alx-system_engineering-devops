#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
                [user_id, username, todo.get("completed"), todo.get("title")]
                )for todo in todos]
