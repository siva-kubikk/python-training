"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

"""
import os

os.system("clear")
a = "For example, say I type the string"
w = a.split()
print(w[::-1])
