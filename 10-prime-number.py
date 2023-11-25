import math, sys

a = int(input("Enter a number to check if it's a Prime number: "))
sqr = int(math.sqrt(a))
for i in range(2, sqr + 1):
    if a % i == 0:
        print(f"{a} is not a Prime number.")
        break
    else:
        continue
else:
    print(f"{a} is a Prime number.")
