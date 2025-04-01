# Join Two Sets

# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# Example:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) 

print(set3)

# The union() method returns a new set with all items from both sets:

# Example:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)

print(set1) 

# The update() method inserts the items in set2 into set1:

# Example:

set1 = {"a", "b" , "c"} 
set2 = {1, 2, 3}

set1.update(set2)

print(set1)

# Note: Both union() and update() will exclude any duplicate items.

# Example:  

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.union(set2)

print(set1) 

# Intersection

# The intersection() method returns a new set with items that are present in both sets.

# Example:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.intersection(set2)

print(set3)

# The intersection_update() method will keep only the items that are present in both sets.

# Example:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.intersection_update(set2)

print(set1) 


# Difference

# The difference() method returns a set that contains the difference between two sets.

# Example:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.difference(set2)

print(set3)

# The difference_update() method removes the items that exist in both sets.

# Example:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}    

set1.difference_update(set2)

print(set1)

# Symmetric Difference

# The symmetric_difference() method returns a set that contains all items from both sets, except items that are present in both sets.

# Example:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.symmetric_difference(set2)

print(set3) 

# The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.

# Example:  

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.symmetric_difference_update(set2)

print(set1) 

# issubset()

# The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.

# Example:  

set1 = {"a", "b" , "c"}
set2 = {"f", "e", "d", "c", "b", "a"}

print(set1.issubset(set2))  

# issuperset()

# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.

# Example:  

set1 = {"f", "e", "d", "c", "b", "a"}
set2 = {"a", "b" , "c"}

print(set1.issuperset(set2))    

# isdisjoint()

# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

# Example:  

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

print(set1.isdisjoint(set2))







