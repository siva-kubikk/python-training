import sys

a = str.lower(input("Player1 choice: "))
b = str.lower(input("Player2 choice: "))

"""
Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""
if a == b:
    print("It's a tie")
elif a == "rock":
    if b == "scissors":
        print(f"Player1({a}) beats Player2({b})")
    elif b == "paper":
        print(f"Player2({b}) beats Player1({a})")
    else:
        print(f"Invalid choice by Player2({b}).")
        sys.exit()
elif a == "scissors":
    if b == "paper":
        print(f"Player1({a}) beats Player2({b})")
    elif b == "rock":
        print(f"Player2({b}) beats Player1({a})")
    else:
        print(f"Invalid choice by Player2({b}).")
        sys.exit()
elif a == "paper":
    if b == "rock":
        print(f"Player1({a}) beats Player2({b})")
    elif b == "scissors":
        print(f"Player2({b}) beats Player1({a})")
    else:
        print(f"Invalid choice by Player2({b}).")
        sys.exit()
else:
    print(f"Invalid choice by Player1({a}).")
    sys.exit()
