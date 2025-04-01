# Sets

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable, and unindexed.

# Sets are written with curly brackets.

# Example:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Set Items

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Example:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Note: Sets are unordered, so you cannot be sure in which order the items will appear. 

# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)  

# Get the Length of a Set

# To determine how many items a set has, use the len() function.

# Example:  

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set Items - Data Types

# Set items can be of any data type:

# Example:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3) 

# A set can contain different data types:

# Example:

set1 = {"abc", 34, True, 40, "male"}    

print(set1)


