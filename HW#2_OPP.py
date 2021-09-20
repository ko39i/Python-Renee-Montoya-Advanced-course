# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class

class Animal():
    def __init__(self, name):
        self.name = name
        print(self.name)

    def eat(self):
        print("animal sleeping")

    def sleep(self):
        print("animal eating")


class Animal1(Animal):
    def hunt(self):
        print("animal hunts")


class Animal2(Animal):
    def run(self):
        print("animal runing")


class Animal3(Animal):
    def growl(self):
        print("animal growls")


class Animal4(Animal):
    def reproduction(self):
        print("animal reproduction")


class Animal5(Animal):
    def jump(self):
        print("animal jumping")


animal1 = Animal1("Cat")
animal1.eat()
animal1.sleep()
animal1.hunt()

animal2 = Animal2("Dog")
animal2.eat()
animal2.sleep()
animal2.run()

animal3 = Animal3("Tiger")
animal3.eat()
animal3.sleep()
animal3.growl()

animal4 = Animal4("Raddit")
animal4.eat()
animal4.sleep()
animal4.reproduction()

animal5 = Animal5("Kangaroo")
animal5.eat()
animal5.sleep()
animal5.jump()

print(isinstance(animal1, Animal))
print(isinstance(animal2, Animal))
print(isinstance(animal3, Animal))
print(isinstance(animal4, Animal))
print(isinstance(animal5, Animal))


# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.

class Human():
    def eat(self):
        print("human sleeping")


    def sleep(self):
        print("human eating")

    def study(self):
        print("human is studying")

    def work(self):
        print("human working")


class Centaur(Animal, Human):
    def bow(self):
        print("Centaur shoots a bow")

centaur = Centaur("Firenze")
centaur.eat()
centaur.bow()
centaur.work()

# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:
    def __init__(self):
        arm1 = Arm(print("R"))
        arm2 = Arm(print("L"))
        self.arms = [arm1, arm2]

class Arm:
    def __init__(self, place):
        self.place = place

person = Person()


class CellPhone:
    def __init__(self):
        self.Screen = Screen

class Screen:
    pass

screen = Screen
phone = CellPhone()


3.
#     Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
#     Override a printable string representation of Profile class and return: list of the params mentioned above
class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Profile: {self.name},{self.last_name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}, {self.sex}"

    def __repr__(self):
        return f"Profile:({self.name},{self.last_name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}, {self.sex})"

profile = Profile('Jon', 'Sina', '4542', '5 Stone Street, Apt. 2A, Jacksonville, FL 39404', 'jon32@mailcom', '12/02/2000', '21', 'F')

print(profile)

# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
from abc import ABC, abstractmethod

class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError

class HPLaptop(Laptop):
    def __init__(self, name):
        self.name = name

    def screen(self):
        print(f'{self.name } have 10 inch screen')

    def keyboard(self):
        print(f'{self.name} have keyboard')

    def touchpad(self):
        print(f'{self.name} have touchpad')

    def webcam(self):
        print(f'{self.name} have webcam')

    def ports(self):
        print(f'{self.name} have USB and Type-S ports')

    def dynamics(self):
        print(f'{self.name} have stereo dynamics')

laptop = HPLaptop("HP")
laptop.screen()
laptop.ports()
laptop.dynamics()







