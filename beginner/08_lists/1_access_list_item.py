# Access Items

# List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Note: The first item has index 0.

# Negative Indexing

# Negative indexing means start from the end.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Note: -1 refers to the last item, -2 refers to the second last item etc.

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Range of Negative Indexes

# Specify negative indexes if you want to start the search from the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Note: -4 refers to the fourth last item, -3 refers to the third last item etc.

# Check if Item Exists

# To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
