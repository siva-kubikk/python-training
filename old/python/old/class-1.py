# import mymodule as mm

# print(dir(mm))

# # g = mm.greeting("Shiva")

# # print(g)

# # f = mm.farewell("Shiva")

# # print(f)


class Dog:
    def __init__(self, name, age):
        self.name1 = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.name1)  # Accessing object attribute
print(my_dog.age)


print(my_dog.bark())  # Calling object method
