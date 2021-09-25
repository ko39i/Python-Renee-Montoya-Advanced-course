import json
from typing import TextIO

from models.plant import Plant
from models.employee import Employee


id = int(input("ID: "))
location = input("Location: ")
name = input("Name: ")
user_file = open('database/employees.json', 'r')
user_data = json.loads(user_file.readline())
user_file.close()
director_email = input("director_email: ")
for email in user_data:
    if director_email != email['email']:
        print("Email not found. Tre again.")
        break
    else:
        continue
director_id = email['id']
plant = Plant(id, location, name, director_id)
plant.save()