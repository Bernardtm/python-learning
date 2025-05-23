# Loop Through a Dictionary

# You can loop through a dictionary by using a for loop.

# Example:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}      

for x in thisdict:
    print(x)

# You can also use the values() method to return values of a dictionary:    

# Example:

for x in thisdict.values():
    print(x)    

# You can use the keys() method to return the keys of a dictionary:

# Example:

for x in thisdict.keys():
    print(x)    

# Loop through both keys and values, by using the items() method:

# Example:

for x, y in thisdict.items():
    print(x, y) 


