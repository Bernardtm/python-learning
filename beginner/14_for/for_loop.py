# For Loop

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Example:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)    

# Looping Through a String

# Even strings are iterable objects, they contain a sequence of characters:

# Example:

for x in "banana":
    print(x)    

# The break Statement

# With the break statement we can stop the loop before it has looped through all the items: 

# Example:

for x in fruits:
    if x == "banana":
        break
    print(x)    

# The continue Statement

# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# Example:

for x in fruits:
    if x == "banana":
        continue
    print(x)    

# The range() Function

# To loop through a set of code a specified number of times, we can use the range() function,

# Example:  

for x in range(6):
    print(x)    

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

# Example:  

for x in range(2, 6):
    print(x)    
