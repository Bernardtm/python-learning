# Nested Dictionaries

# A dictionary can contain dictionaries, this is called nested dictionaries.

# Example:

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)

# Access Items in Nested Dictionaries

# To access items in a nested dictionary, you can use the following syntax:

# Example:  

print(myfamily["child1"]["name"])   

# Change Items in Nested Dictionaries

# You can change the value of a specific item by referring to its key name:

# Example:  

myfamily["child2"]["year"] = 2018

print(myfamily) 

# Add Items to a Nested Dictionary

# You can add a new item to a nested dictionary by referring to its key name:

# Example:  

myfamily["child4"] = {
    "name": "John",
    "year": 2019
}

print(myfamily) 

# Remove Items from a Nested Dictionary

# You can remove an item from a nested dictionary by using the del keyword:

# Example:  

del myfamily["child2"]

print(myfamily) 

# The clear() method empties the dictionary:

# Example:

myfamily.clear()

print(myfamily) 

# Loop through a Nested Dictionary

# You can loop through a nested dictionary by using a for loop.

# Example:  

for x in myfamily:
    print(x)

