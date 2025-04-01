# Copy List 

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes to list1 will automatically also be changes to list2.

# There are ways to make a copy, one way is to use the built-in List method copy().

# Example:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().

# Example:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
