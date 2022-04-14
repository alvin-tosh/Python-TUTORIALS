# A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.
# A tuple is like a list except that it uses parentheses () instead of square brackets []...ie

rgb = ('red', 'green', 'blue')

# Once you define a tuple, you can access an individual element by its index...

print(rgb[0])  # Output red
print(rgb[1])  # Output green
print(rgb[2])  # Output blue

--------------------------------------------------------------------------------------------------------------------------
# Since a tuple is immutable, you cannot change its elements.

rgb = ('red', 'green', 'blue')
rgb[0] = 'yellow'  # attempts to change the first element of the rgb tuple to 'yellow'

print(rgb[0])      # TypeError: 'tuple' object does not support item assignment --- Python throwing a tantrum!

--------------------------------------------------------------------------------------------------------------------------

# To define a tuple with one element, you need to include a trailing comma after the first element...ie
numbers = (3,)
print(type(numbers))   # Output: <class 'tuple'>

# If you exclude the trailing comma, the type of the numbers will be int , which stands for integer. 
# And its value is 3. Python won’t create a tuple that includes the number 3...ie
numbers = (3)
print(type(numbers))   # Output: <class 'int'> --- Python pouts!  

# ASSIGNMENT (of tuples...not Homework ;)
# Even though you can’t change a tuple, you can assign a new tuple to a variable that references a tuple...ie
colors = ('red', 'green', 'blue')
print(colors)   # Output: red green blue

colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)   # Output: Cyan Magenta Yellow black


