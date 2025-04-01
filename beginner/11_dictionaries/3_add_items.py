# Adding Items

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# Example:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}      

thisdict["color"] = "red"

print(thisdict)

# Update Dictionary

# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example:  

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}      

thisdict.update({"color": "red"})

print(thisdict) 




