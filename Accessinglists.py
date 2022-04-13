# This shows you how to access, modify and delete elements in a list.

# ACCESSING ELEMENTS IN A LIST!

# Since a list is an ordered collection, you can access its element by indexes like this
list[index]

# Lists are zero-based index. In other words, the first element has an index 0, the second element has an index 1, and so on.
# For example, the following shows how to access the first element of the numbers list...

numbers = [1, 3, 2, 7, 9, 4]

print(numbers[0])

# Output 
# 1

print(numbers[1]) # will return the second element from the list


# The negative index allows you to access elements starting from the end of the list.
  list[-1] # returns the last element.
  list[-2] # returns the second last element, and so on
  
print(numbers[-1]) # Output 4

print(numbers[-2]) # Output 9



# MODIFYING, ADDING & REMOVING ELEMENTS!

# To change an element, you assign a new value to it using this syntax:
list[index] = new_value

# The example shows how to change the first element of the numbers list to 10

numbers = [1, 3, 2, 7, 9, 4]
numbers[0] = 10

print(numbers)

# Output
# [10, 3, 2, 7, 9, 4]



# The following shows how to multiply the second element with 10...

numbers = [1, 3, 2, 7, 9, 4]
numbers[1] = numbers[1]*10

print(numbers)

# Output
# [1, 30, 2, 7, 9, 4]

# And the following divides the third element by 2
numbers[2] /= 2

# Output
# [1, 3, 1.0, 7, 9, 4]


# The append() method appends an element to the end of a list...ie
numbers = [1, 3, 2, 7, 9, 4]
numbers.append(100)

print(numbers)

# Output
# [1, 3, 2, 7, 9, 4, 100]


# The insert() method adds a new element at any position in the list...ie
numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100) # the following inserts the number 100 at index 2 of the numbers list

print(numbers)

# Output
# [1, 3, 100, 2, 7, 9, 4]










