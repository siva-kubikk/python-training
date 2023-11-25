a = int(input("Enter a number to check if it's a Prime number: \n"))
b = int(input("Enter a number to check for divisors range: \n"))
for i in range(2, b):
    print(i)
    if a != i:
        if a % i == 0:
            print(f"{a} is not a prime number")
            break
        else:
            print(f"{a} is a prime number")
            break

    i += 1
