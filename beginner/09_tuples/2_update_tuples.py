
# Update Tuples

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# But there are some workarounds.

# Convert the tuple into a list, change the list, and convert the list back into a tuple.

# Example:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

# Example:

thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)

# Remove Items

# Note: You cannot remove items in a tuple.

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# Example:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# The del keyword can delete the tuple completely:

# Example:

thistuple = ("apple", "banana", "cherry")
del thistuple
try:
    print(thistuple) # This will raise an error because the tuple no longer exists
except NameError:
    print("The tuple no longer exists")

# Join Two Tuples

# To join two or more tuples you can use the + operator:

# Example:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)



