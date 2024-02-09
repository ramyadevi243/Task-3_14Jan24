'''
Name: Ramya
Date: 18/01/2024
Task: 7
'''

# Write a Python program to find the first non-repeating elements in a given list of integers

# Created a list of items
list = [41, 34, 68, 41, 82, 50, 68, 41, 6, 82, 83]

# Created an empty list
empty = []

# Iterate over the list
for data in list:
    # Append the empty list with items that are not in list 
    if data not in empty:
        empty.append(data)

# Print the non-repeating elements in the list of integers
print("List of non-repeating elements present in the list are: ", empty)