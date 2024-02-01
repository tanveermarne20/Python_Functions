# Example list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Append method
my_list.append(8)
print("Append:", my_list)

# Extend method
my_list.extend([7, 9, 3])
print("Extend:", my_list)

# Insert method
my_list.insert(2, 0)
print("Insert:", my_list)

# Remove method
my_list.remove(9)
print("Remove:", my_list)

# Pop method
popped_value = my_list.pop(4)
print("Pop:", my_list, "Popped Value:", popped_value)

# Index method
index_of_5 = my_list.index(5)
print("Index of 5:", index_of_5)

# Count method
count_of_1 = my_list.count(1)
print("Count of 1:", count_of_1)

# Sort method
my_list.sort()
print("Sorted:", my_list)

# Reverse method
my_list.reverse()
print("Reversed:", my_list)

# Copy method
copied_list = my_list.copy()
print("Copied:", copied_list)
