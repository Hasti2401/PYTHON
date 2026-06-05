import math
import random
import os
from datetime import datetime
import sys

a = int(input("Enter number: "))


print(f"Squareroot of {a} is ", math.sqrt(a))
print(f"ceil of {a} is ",math.ceil(a))
print(f"Floor of {a} is ",math.floor(a))
print(f"Factorial of {a} is ",math.factorial(a))
print(f"Absolute value of {a} is ",math.fabs(a))



print("Random number between 1 to 10: " ,random.randint(1, 10))
print("Random number: " ,random.random())
print("Random number between 1 to 10: " ,random.randrange(1, 10))


print(os.getcwd())
print(os.listdir())
print(os.mkdir("New"))


now = datetime.now()
print(now)


print(sys.version)