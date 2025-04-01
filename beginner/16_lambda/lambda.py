# Lambda

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Example:

x = lambda a : a + 10

print(x(5)) 

# Lambda functions can have multiple arguments:

# Example:  

x = lambda a, b : a * b

print(x(5, 6))

# Lambda functions can be used anywhere a function is expected: 

# Example:

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)   

print(mydoubler(11))    

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# Example:

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))        





