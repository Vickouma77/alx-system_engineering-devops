#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
            } for todo in todos]}, f)
