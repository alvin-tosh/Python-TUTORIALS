# Sometimes, you need to perform a task multiple times in a program. And you don’t want to copy the code for that same task all over places.
# To do so, you wrap the code in a function and use this function to perform the task whenever you need it.

# In practice, you use functions to divide a large program into smaller and more manageable parts. The functions will make your program easier to develop, read, test, and maintain.

# A function definition starts with the def keyword and the name of the function (greet)

def greet ():
  
    #   Display a greeting to users 
    print('Hi there, i am Alvin')


# If the function needs some information to do its job, you need to specify it inside the parentheses (). 
# The greet function in this example doesn’t need any information, so its parentheses are empty. 

# !!!!!!!!! The function definition always ends in a colon (:) !!!!!!!!!!

# All the indented lines that follow the function definition make up the function’s body.

# The text string surrounded by triple quotes is called a docstring. It describes what the function does. Python uses the docstring to generate documentation for the function automatically.
# The line print('Hi') is the only line of actual code in the function body. The greet() function does one task: print('Hi').

# CALLING A FUNCTION
# When you want to use a function, you need to call it. A function call instructs Python to execute the code inside the function.
# The following example calls the greet() function. Since the greet() function doesn’t need any information, you need to specify empty parentheses like this:

greet()

