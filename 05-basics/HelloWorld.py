__author__= 'adr'
print('Hello, World!')
print(1 + 2)
print(7 * 6)
print()
print("The End")
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")

greeting = "Hello"
name = "Bruce"

print(greeting + name)
# This is a comment
print(greeting +  ' ' +  name)

greeting = "Hello"
name = input("Please enter your name ")
print(greeting + ' ' + name)

splitString = "This string has been\nsplit over\nseveral"
print(splitString)

tabbedString = "1\t2\t3\t4\t"
print(tabbedString)

anotherSplitString = """This string has been
split over
several lines"""
print(anotherSplitString)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])