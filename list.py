# Creating a list
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Accessing elements from the list
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Modifying elements in the list
my_list[0] = 10
print("Modified list:", my_list)

# Adding elements to the list
my_list.append(6)
print("After appending:", my_list)

# Removing elements from the list
my_list.remove(6)
print("After removing:", my_list)

# Checking if an element is in the list
print("Is 10 in the list?", 10 in my_list)

# Finding the index of an element
print("Index of 10:", my_list.index(10))

# Sorting the list
my_list.sort()
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)

# Length of the list
print("Length of the list:", len(my_list))

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)