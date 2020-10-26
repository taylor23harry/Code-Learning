import random

file = "E:\\Code\\Code\\Python\\Projects\\log.txt"
name_list = "E:\\Code\\Code\\Python\\Projects\\names.txt"
names = []
class Dog:
    """Main dog class."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def present(self):
        """Prints a short message presenting the different attributes of the instance."""
        print(f"My name is {self.name.title()}, and I am {self.age} years old.")

with open(name_list, "r") as file_object:
    lines = file_object.readlines()
    for line in lines:
        names.append(line.strip())

with open(file, "w") as file_object:
    for name in names:
        dogs = [Dog(name, random.randint(1,12))]
        for dog in dogs:
            file_object.write(f"My name is {dog.name} and I am {dog.age} years old.\n")