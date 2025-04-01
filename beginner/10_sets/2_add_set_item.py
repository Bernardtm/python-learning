# Add Set Items

# Once a set is created, you cannot change its items, but you can add new items.

# To add one item to a set use the add() method.

# Example:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)  

# To add items from another set into the current set, use the update() method.

# Example:  

thisset = {"apple", "banana", "cherry"}

thisset.update({"orange", "mango", "pineapple"})

print(thisset)  

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# Example:  

thisset = {"apple", "banana", "cherry"}

mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)  


