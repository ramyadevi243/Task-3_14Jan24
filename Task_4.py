'''
Name: Ramya
Date: 18/01/2024
Task: 4
'''

# Write a python program to to find the sum of first and last digit of an integer

# Input an integer from the user
integer = int(input("Please enter the digit: "))

# Convert the datatype of the integer from int to string
input_string = str(integer)

# Returning the values of first and last digits of string based on index,
# Then converted the datatype from string to int and stored it in 2 variables
first_digit = int(input_string[0])
second_digit = int(input_string[-1])

# Using arithmetic operator returned the sum of 2 digits and stored it in the variable sum
sum = first_digit + second_digit

# Print the sum of first and last digit of the integer
print("Sum of first and last digit of the integer is: ", sum)


