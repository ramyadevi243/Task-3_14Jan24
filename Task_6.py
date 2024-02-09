'''
Name: Ramya
Date: 18/01/2024
Task: 6
'''

# Create 3 lists and find the duplicates in those 3 lists

# Created 3 lists of items
list_1 = [2, 7, 7, 3, 9, 4, 5]
list_2 = [3, 7, 4, 1, 8, 8, 2]
list_3 = [4, 1, 7, 7, 3, 5, 6]

# Created an empty list
duplicate_list = []

# Iterate over list_1
for data in list_1:
    # Check if items of list_1 are common in both list_2 and list_3
    if data in list_2 and data in list_3:
        # Append duplicate list with items that are not already present in duplicate list
        if data not in duplicate_list:
            duplicate_list.append(data)

# Print the list with duplicate items
print("List of items that are duplicate in 3 lists are: ", duplicate_list)