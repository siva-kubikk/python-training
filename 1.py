# # # print("hello world")


# # # def check_even_odd(number):
# # #   if number %2 == 0:
# # #     print("Number " + str(number) + " is even")
# # #   else:
# # #     print("Number " + str(number) + " is odd")

# # # check_even_odd(10)
# # # check_even_odd(101)


# # # n1 = input("Enter first number: ")
# # # n2 = input("Enter second number: ")

# # # sum = int(n1) + int(n2)
# # # diff = int(n1) - int(n2)
# # # product = int(n1) * int(n2)
# # # quotient = int(n1) / int(n2)
# # # print("Sum = " + str(sum))
# # # print("Difference = " + str(diff))
# # # print("Product = " + str(product))
# # # print("Quotient = " + str(quotient))


# # print(round(123212312.11233,4))


# # # num = int(input("Enter a number: "))
# # num = 6
# # factorial = 1

# # for i in range(1, num + 1):
# #     factorial *= i

# # print(f"The factorial of {num} is {factorial}.")


# # for i in range(0,10):
# #     print(i+1)


# # print("Fibonacci")    
# # def fibonacci(n):
# #     a, b = 0, 1
# #     while a < n:
# #         print(a, end=' ')
# #         a, b = b, a + b
# #     print()

# # fibonacci(100)

# # print("\nMin Max")
# # numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# # s = sorted(numbers)
# # print(s)

# # u = set(numbers)

# # print(u)
# # print(f"Max = {max(u)}")
# # print(f"Min = {min(u)}")

# # x=[]
# # for i in numbers:
# #     if i not in x:
# #         x.append(i)

# # print(sorted(x))



# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# print(words)

# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)


# with open('1.py','r') as file:
#   content = file.read()

# print(content)


# lines = ["First line", "Second line", "Third line"]
# with open('1.txt','w') as file:
#   for line in lines:
#     file.write(line + '\n')

# with open('1.txt','r') as file:
#   content = file.read()
#   print(content)



# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
#     print(f"The result is {result}")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")


my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)
my_set.discard(1)
print(my_set)
my_set.add(10)
print(my_set)