''' 1)Create a python program to sort the given list of tuples based on integer value using a lambda 
function. [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), 
('Virat Kohli', 24936)]'''

player_scores = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_list = sorted(player_scores, key=lambda x: x[1])
print("Sorted list based on scores:")
print(sorted_list)