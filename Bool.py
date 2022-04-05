# In programming you often need to know if an expression is True or False. 
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer

print(10 > 9)  # True
print(10 == 9) # False 
print(10 < 9)  # False



# The bool() function allows you to evaluate any value, and give you True or False in return.
x = "Hello"
y = 15

print(bool(x)) # True
print(bool(y)) # True



# Almost any value is evaluated to True if it has some sort of content.
.......................................................................
# Any string is True, except empty strings.
......................................................................
# Any number is True, except 0.
......................................................................
# Any list, tuple, set, and dictionary are True, except empty ones.
......................................................................
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# All will return True



#FYI: There are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 
# All will return False
