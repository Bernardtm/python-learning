# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Getting the data type
x = 5
print(type(x))

# Setting the data type
x = str("Hello World")
print(type(x))

x = str("""
Hello
World
""")
print(type(x))


# Setting the data type
x = int(20)
print(type(x))  

# Setting the data type
x = float(20.5)
print(type(x))

# Setting the data type
x = complex(1j)
print(type(x))  

# Setting the data type
x = list(("apple", "banana", "cherry"))
print(type(x))

# Setting the data type
x = tuple(("apple", "banana", "cherry"))
print(type(x))  

# Setting the data type
x = range(6)
print(type(x))

# Setting the data type
x = dict(name="John", age=36)
print(type(x))  

# Setting the data type
x = set(("apple", "banana", "cherry"))
print(type(x))

# Setting the data type 
x = frozenset(("apple", "banana", "cherry"))
print(type(x))

# Setting the data type
x = bool(5)
print(type(x))

# Setting the data type
x = bytes(5)
print(type(x))

# Setting the data type
x = bytearray(5)
print(type(x))  

# Setting the data type
x = memoryview(bytes(5))
print(type(x))  

# Setting the data type
x = None
print(type(x))  


# Setting the Specific Data Type
x = str("Hello World")
print(x)

x = int(20)
print(x)

x = float(20.5)
print(x)

x = complex(1j)
print(x)    

x = list(("apple", "banana", "cherry"))
print(x)

x = tuple(("apple", "banana", "cherry"))
print(x)    

x = range(6)
print(x)

x = dict(name="John", age=36)
print(x)    

x = set(("apple", "banana", "cherry"))
print(x)

x = frozenset(("apple", "banana", "cherry"))
print(x)    

x = bool(5)
print(x)

x = bytes(5)
print(x)    

x = bytearray(5)
print(x)    

x = memoryview(bytes(5))
print(x)  

