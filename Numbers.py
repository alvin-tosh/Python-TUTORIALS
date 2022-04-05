# There are three numeric types in Python; Variables of numeric types are created when you assign a value to them

x = 1     # int or integer, is a whole number, positive or negative, without decimals, of unlimited length.
y = 2.8   # float or "floating point number" is a number, positive or negative, containing one or more decimals.
a = 35e3  # Float can also be scientific numbers with an "e" to indicate the power of 10
z = 1j    # complex numbers are written with a "j" as the imaginary part

# To verify the type of any object in Python, use the type() function
print(type(x))
print(type(y))
print(type(z))



# Type Conversion: You can convert from one type to another with the int(), float(), and complex() methods.
# NOTE: You cannot convert complex numbers into another number type!
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 



# Python has a built-in module called random that can be used to make random numbers.
import random

print(random.randrange(1, 10)) # ImportS the random module, and displayS a random number between 1 and 9
