# Removing Items

# There are several methods to remove items from a dictionary:

# Example:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}      

thisdict.pop("model")

print(thisdict) 

# The popitem() method removes the last item:

# Example:

thisdict.popitem()  

print(thisdict)

# The del keyword removes the item with the specified key name:

# Example:  

del thisdict["model"]

print(thisdict)

# The clear() method empties the dictionary:    

# Example:

thisdict.clear()

print(thisdict) 




