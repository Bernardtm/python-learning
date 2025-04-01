# List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax

# newlist = [expression for item in iterable if condition == True]

# The condition is optional and can be omitted.

# Example:  

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Iterable  

# The iterable can be any iterable object, like a list, tuple, set etc.

# Example:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)      

# Condition

# The condition is optional and can be omitted.

# Example:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Expression    

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like in the new list.

# Example:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# Iterable

# The iterable can be any iterable object, like a list, tuple, set etc.

# Example:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
