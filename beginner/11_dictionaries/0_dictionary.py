# Dictionaries

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Example:  

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   

print(thisdict)

# Ordered or Unordered?

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.  

# Unordered means that the items do not have a defined order, and the order can change.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.    

# Dictionary Length

# To determine how many items a dictionary has, use the len() function.

# Example:  

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   

print(len(thisdict))

# Changeable

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Example:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   

thisdict["year"] = 2018

print(thisdict) 

# Duplicates Not Allowed

# Dictionaries cannot have two items with the same key:

# Example:  

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}      

print(thisdict)

# Type

# A dictionary can contain different data types:

# Example:

thisdict = {
    "brand": "Ford",    
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}   

print(type(thisdict))

# The dict() Constructor

# It is also possible to use the dict() constructor to make a dictionary.

# Example:

thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict)



