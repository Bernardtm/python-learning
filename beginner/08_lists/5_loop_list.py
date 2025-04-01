# Loop Through a List

# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])    

# Using a While Loop

# You can loop through the list items by using a while loop.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1        
