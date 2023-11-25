import random

a = ""
num = random.randint(1, 9)

while a != "exit" and a != num:
    a = input("Guess a number between 1 and 9: ")
    if a == "exit":
        break
    elif a == "":
        print("No input entered.\n")
        continue
    print(f"Generated number is {num}")

    if int(a) == num:
        print(f"You guessed the correct number {num}.\n")
        continue
    elif int(a) < num:
        print(f"Your guess {a} is lower than {num}.\n")
        continue
    elif int(a) > num:
        print(f"Your guess {a} is higher than {num}.\n")
        continue
