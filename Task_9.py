'''
Name: Ramya
Date: 18/01/2024
Task: 9
'''

# Given a python list and a value of 59, write a python program to find the triplet
# in the list whose sum is equal to the given value.

# Given list
list = [10,20,30,9]

# Sum of triplet
sum_of_triplet = 59

# Initializing a variable n which stores the length of list
n = len(list)

# Creating an empty list which will store the triplet substring
empty = []

# Iterating over the list from a range of index from 0 to n
for i in range(n):
    # Iterates over the inner loop of j, where j starts from the next index of i
    for j in range(i+1, n):
        # Iterates over inner loop of j, where k starts from the next index of j
        for k in range(j+1, n):
            # Check if value of sum of any combination of triplets is equal to sum
            if (list[i] + list[j] + list[k]) == sum_of_triplet:
                # If yes, then append the list to empty list
                empty.append((list[i], list[j], list[k]))

# Print the triplet
print("The triplet whose sum is equal to 59 is: ", empty)