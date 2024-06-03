import random, string

# a = int(input("Enter password length: "))

a = random.randint(10, 30)
p = []


for i in range(0, a):
    special_char = random.choice(string.punctuation)
    number = str(random.randint(0, 9))
    upper_case = random.choice(string.ascii_uppercase)
    lower_case = random.choice(string.ascii_lowercase)
    p.append(random.choice((special_char, number, upper_case, lower_case)))

print("".join(random.sample(p, a)))
