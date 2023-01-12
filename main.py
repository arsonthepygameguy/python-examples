#tTis program was made by parker anderson

#Import the turtle and randint
import turtle as turt
from random import randint as rand

#Find the factorial of a given number
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


print("examples of thing you can do in python:")
print("factorials")
print("drawing")

#Do different mini-programs based off user input
Example_Programs = input("what program would you like?: ")
if Example_Programs == "factorials":
	NUM = input("what number do you want?: ")
	print(factorial(NUM))
	
elif Example_Programs == "drawing":
	for i in range(14):
		turt.circle(10)
		turt.right(25)