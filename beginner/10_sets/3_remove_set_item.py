# Remove Set Items

# To remove an item in a set, use the remove(), or the discard() method.

# Example:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)  

# Note: If the item to remove does not exist, remove() will raise an error.

# Example:  

thisset = {"apple", "banana", "cherry"}

thisset.remove("orange")

print(thisset)  

# Note: If the item to remove does not exist, remove() will raise an error.

# To avoid this error, use the discard() method.

# Example:  

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)  

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# Example:  

thisset = {"apple", "banana", "cherry"}

thisset.discard("orange")

print(thisset)      

# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.

# Example:  

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)    

print(thisset)  

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.   

# Example:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()   

print(x)    

print(thisset)  

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.   

# The clear() method empties the set:

# Example:

thisset = {"apple", "banana", "cherry"} 

thisset.clear()

print(thisset)  

# The del keyword will delete the set completely:   

# Example:

thisset = {"apple", "banana", "cherry"}

del thisset 

try:
    print(thisset)  
except NameError:
    print("The set no longer exists")







