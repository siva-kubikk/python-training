'''
Data Filter: Given a list of numbers, write a program to filter out all the numbers greater than a specific number provided by the user.
'''
num_list = [1,2,4,5,6,6,3,434,43,34,34,3,3,456,7,9,9,7,7,7,68,3]
result=set() # Using a set automatically removes duplicates
a = input("Enter a number: ")

for i in num_list:
    if i > int(a):
        result.add(i)
        
print(sorted(result))