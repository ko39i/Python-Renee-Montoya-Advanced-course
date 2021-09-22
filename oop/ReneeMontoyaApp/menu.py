from models.plant import Plant
from models.employee import Employee
import json

user_file = open('database/employees.json', 'r')
user_data = json.loads(user_file.readline())
user_file.close()

if __name__ == '__main__':
    while True:
        print(
            "Choose a menu item by number: \n" +
              "1. Add new Plant \n" +
              "2. Add new Employee \n" +
              "3. Get plant by id \n" +
              "4. Get employee by id \n"
              )
        menu_flag = int(input("Your choose: "))
        if menu_flag == 1:
            id = int(input("ID: "))
            location = input("Location: ")
            name = input("Name: ")
            user_file = open('database/employees.json', 'r')
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
        elif menu_flag == 2:
            id = int(input("ID: "))
            name = input("Name: ")
            email = input("Email: ")
            department_type = input("Department Type: ")
            department_id = int(input("Department id: "))
            employee = Employee(id, name, email, department_type, department_id)
            employee.save()
        elif menu_flag == 3:
            id = int(input("ID: "))
            plant = Plant.get_by_id(id)
            print(plant)
        elif menu_flag == 4:
            id = int(input("ID: "))
            employee = Employee.get_by_id(id)
            print(employee)
