"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

"""
import random


def create_random_size_list():
    num_list = []
    list_size = random.randint(5, 25)
    print(list_size)
    for i in range(0, list_size):
        num_list.append(random.randint(i, 1000))
    return num_list


a = create_random_size_list()
print(a)


def list_ends(a):
    result = []
    result = (a[0], a[-1])
    print(result)


list_ends(a)
