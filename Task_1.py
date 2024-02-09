'''
Name: Ramya
Date: 18/01/2024
Task: 1
'''

# Create 2 lists from the given list, one with odd numbers and the other with even numbers

# Given list
list = [10, 501, 22, 37, 100, 999, 87, 351]
# Creating 2 empty lists, one for odd numbers and another for even numbers
odd_list = []
even_list = []

# Iteration over the list
for data in list:
    # Using conditional statement, checking if elements in list is even number
    if data % 2 == 0:
        # If even number, then add the number to even_list
        even_list.append(data)
    # If not even, then add the element to odd_list
    else:
        odd_list.append(data)

# Print the 2 lists for odd and even numbers
print(f"List with odd numbers: {odd_list}")
print(f"List with even numbers: {even_list}")