from models.plant import Plant
from models.employee import Employee
import json


class Controller:
    def add_plant(self):
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

    def add_employee(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    def get_plant(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    def get_employee(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)

controller = Controller()

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
            controller.add_plant()
        elif menu_flag == 2:
            controller.add_employee()
        elif menu_flag == 3:
            controller.get_plant()
        elif menu_flag == 4:
            controller.add_employee()
