# An Empty List
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15) # insert at index 1 (second position)

# Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

# Remove the last element from my_list.
my_list.pop() # removes the last element

# Sort my_list in ascending order.
my_list.sort() # Sorts in ascending order

# Find and print the index of the value 30 in my_list.
# print (my_list.index(30))
my_index = my_list.index(30)
print(f"The position of value 30 on the list is at index:", my_index)
