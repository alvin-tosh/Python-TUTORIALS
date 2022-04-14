# A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.
# A tuple is like a list except that it uses parentheses () instead of square brackets []...ie

rgb = ('red', 'green', 'blue')

# Once you define a tuple, you can access an individual element by its index...

print(rgb[0])  # Output red
print(rgb[1])  # Output green
print(rgb[2])  # Output blue

# Since a tuple is immutable, you cannot change its elements.

rgb = ('red', 'green', 'blue')
rgb[0] = 'yellow'  # attempts to change the first element of the rgb tuple to 'yellow'

print(rgb[0])      # TypeError: 'tuple' object does not support item assignment

