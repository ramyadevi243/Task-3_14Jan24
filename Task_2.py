'''
Name: Ramya
Date: 18/01/2024
Task: 2
'''

# Count all the prime numbers from the list and create a new Python list
# containing all the prime numbers in it

# This is the given list
given_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Created an empty list
prime_numbers = []

# Initiated a variable called count with value 0
count = 0

# Iterated over the list
for num in given_list:
    # Iterated over the variable num from 2 till num-1
    for number in range(2, num):
        # Using conditional statement, checked if num variable is divisible by variable number
        # Logic to check if num is a prime number or not
        if (num % number) == 0:
            # If yes, then it is not a prime number
            # break from loop
            break
    # Else, append the count with value 1 each time a number is a prime number
    # Also, append the empty list with prime number
    else:
        count = count + 1
        prime_numbers.append(num)

# print the new list of prime numbers
print("Prime numbers in the given list are: ", prime_numbers)

# print the length of list
print("Length of the list is: ", len(prime_numbers))

# Print the count of prime numbers in list
print("Count of prime numbers: ",count)