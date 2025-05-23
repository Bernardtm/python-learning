
# Python Tuples

# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Dictionary, and Set.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Example:


thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items

# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Duplicate Values

# Since tuples are indexed, they can have items with the same value:

# Example:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length

# To determine how many items a tuple has, use the len() function:

# Example:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma, even though there is only one item:

# Example:

thistuple = ("apple",)
print(type(thistuple))

# Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")

# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple.

# Example:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

# List
# Tuple
# Set
# Dictionary
# When choosing a collection type, it is useful to understand the properties of that type.








