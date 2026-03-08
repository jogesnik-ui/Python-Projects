import json


tasks = {
    "Maths": {
    "description": "All of 1L",
    "due-date": "Tomorrow"
    },
    "English": {
        "description": "Critical Reading Test",
        "due-date": "Thursday"
    }
}

with open("Assignments.json", 'w') as file:
    json.dump(tasks, file, indent=4)

with open("Assignments.json", 'r') as file:
    tasks = json.load(file)
    print(tasks)