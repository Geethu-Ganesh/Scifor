''' 3)Write a python program to convert the given list of integers into a tuple of strings. Use map 
and lambda functions Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] '''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string_numbers = map(lambda x: str(x), numbers)
tuple_of_strings = tuple(string_numbers)
print("Tuple of strings:")
print(tuple_of_strings)