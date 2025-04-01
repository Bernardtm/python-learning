# Accessing Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   

print(thisdict["brand"])    

# There is also a method called get() that will give you the same result:

# Example:  

print(thisdict.get("brand"))

# Get Keys

# The keys() method will return a list of all the keys in the dictionary.   

# Example:

print(thisdict.keys())

# Get Values

# The values() method will return a list of all the values in the dictionary.

# Example:

print(thisdict.values())    

# Get Items

# The items() method will return each item in a dictionary, as tuples in a list.

# Example:  

print(thisdict.items())

# Check if Key Exists

# To determine if a specified key exists in a dictionary use the in keyword:    

# Example:

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict")    



