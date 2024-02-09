'''
Name: Ramya
Date: 18/01/2024
Task: 3
'''

# Given a Python list, find out how many numbers are Happy Numbers

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Created an empty list
happy_numbers = []

# Function to check if a number is happy
def is_happy(num):
    # Using while loop and 'and' logical operator, check if a particular number is not 1 and 4
    # If not 1 and 4, then enter the loop
    while num != 1 and num != 4:
        num = sum(int(digits)**2 for digits in str(num))
    # Return only if the sum is equivalent to 1
    return num == 1

# Iteration over the list
for num in numbers:
    # Using conditional statement, if the number is a happy number
    # then append to the empty list
    if is_happy(num):
        happy_numbers.append(num)

# Print the list of Happy Numbers in a new list
print("Happy numbers in the list:", happy_numbers)
