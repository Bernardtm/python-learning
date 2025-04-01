# Functions

# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# Creating a Function

# In Python a function is defined using the def keyword:    

# Example:

def my_function():
    print("Hello from a function")  

# Calling a Function

# To call a function, use the function name followed by parenthesis:

# Example:  

my_function()

# Arguments

# Information can be passed into functions as arguments.    

# Example:

def my_function(fname):
    print(fname + " Refsnes")   

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of Arguments   

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# Example:  

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")  

# Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# Example:  

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")  

# Keyword Arguments

# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.  

# Example:

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")   

# Arbitrary Keyword Arguments, **kwargs 

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# Example:

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.


# Default Parameter Value

# The following example shows how to use a default parameter value. If we call the function without argument, it uses the default value:

# Example:  

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()

# Passing a List as an Argument

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# Example:  

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values

# To let a function return a value, use the return statement:   

# Example:

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))   

# The pass Statement

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example:  

def myfunction():
    pass

# Positional-Only Arguments

# In Python, positional-only arguments are a feature that allows developers to specify that certain parameters must be passed by position only, rather than by name. This is particularly useful in cases where the order of parameters is important and should not be changed.

# Example:

def add(a, b, /):
    return a + b

# Keyword-Only Arguments

# In Python, keyword-only arguments are a feature that allows developers to specify that certain parameters must be passed by name only, rather than by position. This is particularly useful in cases where the order of parameters is not important and should not be enforced.

# Example:  

def add(a, b, *, c):
    return a + b + c

# Combined Positional and Keyword Arguments 

# In Python, combined positional and keyword arguments are a feature that allows developers to specify that certain parameters must be passed by position only, rather than by name. This is particularly useful in cases where the order of parameters is important and should not be changed.

# Example:

def add(a, b, /, c, *, d):
    return a + b + c + d




# Recursion

# Python also accepts function recursion, which is a function that calls itself.

# This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming. 

# Example:

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result   

print("\n\nRecursion Example Results")
tri_recursion(6)        



