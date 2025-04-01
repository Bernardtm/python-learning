
# Access Tuple Items

# You can access tuple items by referring to the index number, inside square brackets:

# Example:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Note: The first item has index 0.

# Negative Indexing

# Negative indexing means start from the end.

# Example:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Note: -1 refers to the last item, -2 refers to the second last item etc.

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.   

# When specifying a range, the return value will be a new tuple with the specified items.

# Example:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Range of Negative Indexes

# Specify negative indexes if you want to start the search from the end of the tuple:

# Example:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Note: The search will start at index -4 (included) and end at index -1 (not included).

# Check if Item Exists

# To determine if a specified item is present in a tuple use the in keyword:

# Example:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")







