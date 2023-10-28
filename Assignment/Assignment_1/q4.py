''' 4)Write a python program using reduce function to compute the product of a list containing 
numbers from 1 to 25.'''

from functools import reduce
numbers = list(range(1, 26))
product_result = reduce(lambda x, y: x * y, numbers)
print("The product of numbers from 1 to 25 is:")
print(product_result)