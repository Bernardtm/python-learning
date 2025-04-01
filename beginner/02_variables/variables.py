x = 5 # type int
y = "Hello" # type str
y = 'Hello' # type str

print(x)
print(y)

# Casting
x = str(3)
y = int(3)
z = float(3)

print(type(x))
print(type(y))
print(type(z))

# Multiple variables
a = b = c = 1

# Multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# Unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)


# Global and local variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# Global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)