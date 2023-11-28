class Animal:
    def __init__(self,name,species,age) -> None:
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"{self.name} is a {self.species}. It's age is {self.age}.")


class Shelter:
    def __init__(self) -> None:
        self.animals=[]

    def add_animal(self,animal):
        self.animals.append(animal) 
        print(f"{animal.name}({animal.species}) is added to shelter.")


    def display_all_animals(self):
        for animal in self.animals:
            animal.display_info()

a = Animal('Julie','Dog',6)
b = Animal('Bob','Hen',3)
c = Animal('Cathy','Cat',12)
d = Animal('Dan','Mouse',15)

a.display_info()

s = Shelter()
s.add_animal(a)
s.add_animal(b)
s.add_animal(c)
s.add_animal(d)

s.display_all_animals()
