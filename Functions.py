# Sometimes, you need to perform a task multiple times in a program. And you don’t want to copy the code for that same task all over places.
# To do so, you wrap the code in a function and use this function to perform the task whenever you need it.

# In practice, you use functions to divide a large program into smaller and more manageable parts. The functions will make your program easier to develop, read, test, and maintain.

# A function definition starts with the def keyword and the name of the function (greet)

def greet ():
  
    #   Display a greeting to users 
    print('Hi there, i am Alvin!')


# If the function needs some information to do its job, you need to specify it inside the parentheses (). 
# The greet function in this example doesn’t need any information, so its parentheses are empty. 

# !!!!!!!!! The function definition always ends in a colon (:) !!!!!!!!!!

# All the indented lines that follow the function definition make up the function’s body.

# The text string surrounded by triple quotes is called a docstring. It describes what the function does. Python uses the docstring to generate documentation for the function automatically.
# The line print('Hi') is the only line of actual code in the function body. The greet() function does one task: print('Hi').

# CALLING A FUNCTION!
# When you want to use a function, you need to call it. A function call instructs Python to execute the code inside the function.
# The following example calls the greet() function. Since the greet() function doesn’t need any information, you need to specify empty parentheses like this:

greet()

# If you run the program, it’ll show a greeting on the screen

Hi there, i am Alvin!


# RETURNING A VALUE!
# A function can perform a task like the greet() function. Or it can return a value. The value that a function returns is called a return value.
# To return a value from a function, you use the return statement inside the function body.
return value

# This is best explained using functions with multiple parameters

# FUNCTIONS WITH MULTIPLE PARAMETERS!
# A function can have zero, one, or multiple parameters.
# The following example defines a function called sum() that calculates the sum of two numbers:

# In this example, the sum() function has two parameters a and b, and returns the sum of them.
def sum(a, b):
    return a + b

# In the following function call, a will be 10 and b will be 20 inside the function body.
total = sum(10,20)
print(total)

# Output
30


# SUMMARY
    # A Python function is a reusable named block of code that performs a task or returns a value.
    # Use the def keyword to define a new function. A function consists of function definition and body.
    # A function can have zero or more parameters. If a function has one or more parameters, you need to pass the same number of arguments into it.
    # A function can perform a job or return a value. Use the return statement to return a value from a function.


