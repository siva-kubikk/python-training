import json

with open("birthdays.json", "r") as file:
    j = json.load(file)

    print("We have the list of birthdays for the below persons:")
    for key in j:
        print(key)

    a = input("Whose birthday do you want to know?")
    if a in j:
        print(f"{a}'s birthday is {j[a]}.")
