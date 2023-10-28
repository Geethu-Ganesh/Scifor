''' 6)Write a python program to find palindromes in the given list of strings using lambda and filter
function. ['python', 'php', 'aba', 'radar', 'level']'''

words = ['python', 'php', 'aba', 'radar', 'level']
palindromes = list(filter(lambda x: x == x[::-1], words))
print("Palindromes in the list:")
print(palindromes)