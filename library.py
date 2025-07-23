# Library
# python libray is a collection of modules and packages that provide reusable code for various functionalities.
# Example: Using the math library to perform mathematical operations

import math
print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))


# random library
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice from a



# datetime library
import datetime
tomorrow = datetime.date.today() #+ datetime.timedelta(days=1)
print(tomorrow)
print (tomorrow.day)  # Current date and time
import numpy as np

# Create a simple array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)
