
# Unpack Tuples

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Example:

fruits = ("apple", "banana", "cherry")

# But, if we want to assign the values in a tuple to variables, we can do that by unpacking.

# Example:

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example:

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until there are values left.   

# Example:

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Python also allows you to extract the values back into a tuple.

# Example:

fruits = ("apple", "banana", "cherry")  

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# The zip() Function

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new tuple.










