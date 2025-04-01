print("Hello")
print('Hello')

# Single quote in double quotes
print("He is called 'Johnny'")

# Double quote in single quotes
print('He is called "Johnny"')

# Triple quotes
print("""
Hello
World
""")

# Triple quotes
print('''
Hello
World
''')    


# String as an array
a = "Hello, World!"
print(a[1])

# Loop through a string
for x in "banana":
    print(x)

# String length
print(len(a))

# Check if "free" is present in the following text
txt = "The best things in life are free!"
print("free" in txt)

# Check if "expensive" is NOT present in the following text
txt = "The best things in life are free!"
print("expensive" not in txt)

# Slicing
b = "Hello, World!"
print(b[2:5])

# Slice from the start
b = "Hello, World!"
print(b[:5])

# Slice to the end
b = "Hello, World!"
print(b[2:])

# Negative indexing
b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

# Remove whitespace
a = " Hello, World! "
print(a.strip())

# Replace string
a = "Hello, World!"
print(a.replace("H", "J"))

# Split string
a = "Hello, World!"
print(a.split(","))

# String Concatenation
a = "Hello"
b = "World"
print(a + b)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# F-String
name = "John"
age = 36
txt = f"Hello, my name is {name}, and I am {age} years old."
print(txt)

# A placeholder can include a format specifier that allows you to format the value:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {0} pieces of item {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# A placeholder can contain python code, like math operations:
x = 5
y = 10
print(f"The sum of {x} and {y} is {x + y}")

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Escape Character
txt = 'It\'s alright.'
print(txt)














