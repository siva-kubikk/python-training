import random

# a = random.randint(1, 100)
# print(a)

# b = random.random()
# print(b)

# print(random.randint(1, 1000))


def create_random_size_list():
    num_list = []
    list_size = random.randint(5, 15)
    print(list_size)
    for i in range(0, list_size):
        num_list.append(random.randint(i, 1000))
    return num_list


a = create_random_size_list()
b = create_random_size_list()

print(set(a))
print(b)
