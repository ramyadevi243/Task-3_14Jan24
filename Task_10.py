'''
Name: Ramya
Date: 18/01/2024
Task: 10
'''

# Given a list[4,2,1,-3,6] write a python program to find if there is a sub-list with
# sum equal to zero.

# Given list
list = [4, 2, 1, -3, 6]

# Initializing a variable n which stores the length of list
n = len(list)

# Iterate over the length of list
for i in range(n):
    # Initializing sum to be equal to 0
    sum = 0
    # Iterating over the inner loop of i
    for j in range(i,n):
        # Adding the sum of index value of j with sum
        sum = sum + list[j]
        # Checking if sum is equal to zero.
        if sum == 0:
            # If yes, then print the statement and exit the loop
            print("Sublist with sum zero exists")
            exit()

# Else, print this statement
print("No sublist with sum zero exists")