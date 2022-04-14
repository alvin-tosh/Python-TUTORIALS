---------------------------------------------------------------------------------------------------------------------------------------------
# To sort a list, you use the sort() method:
listname.sort()

# sort() method modifies the order of elements in the list.
# By default, the sort() method sorts the elements of a list using the less-than operator (<). 
# In other words, it places the lower elements before the higher ones.

# To sort elements from higher to lower, you pass the reverse=True argument to the sort()...ie
listname.sort(reverse=True)

---------------------------------------------------------------------------------------------------------------------------------------------
# Perhaps a few examples ama....

# 1. If a list contains strings, the sort() method sorts the string elements alphabetically...ie
  guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
  guests.sort()

  print(guests)   # Output: ['James', 'Jennifer', 'John', 'Mary', 'Patricia', 'Robert']
  
---------------------------------------------------------------------------------------------------------------------------------------------  
# 2. sort() method with the reverse=True argument to sort the elements in the guests list in the reverse alphabetical order 
  guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
  guests.sort(reverse=True)

  print(guests)   # Output: ['Robert', 'Patricia', 'Mary', 'John', 'Jennifer', 'James'] ----- See, it reversed the thing!
  
---------------------------------------------------------------------------------------------------------------------------------------------  
# 3. If a list contains numbers, the sort() method sorts the numbers from smallest to largest.
  scores = [5, 7, 4, 6, 9, 8]
  scores.sort()

  print(scores)   # Output: [4, 5, 6, 7, 8, 9]
  
---------------------------------------------------------------------------------------------------------------------------------------------  
# 4. If a list contains tuples, the sort() method needs a sort key function...ie
   
  companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]
  
  # define a sort key  ----  Note that you just pass the function name without the parentheses to the sort() method
    def sort_key(company):
        return company[2]
      
  # The sort() method will use the value returned by the sort_key() function for the comparisons.
    # sort the companies by revenue
      companies.sort(key=sort_key, reverse=True)

    # show the sorted companies
      print(companies)   # Output: [('Apple', 2019, 260.2), ('Google', 2019, 134.81), ('Facebook', 2019, 70.7)]
      
---------------------------------------------------------------------------------------------------------------------------------------------      
# 5. Using lambda expression --- To make it more concise, Python allows you to define a function without a name using...
  lambda arguments: expression
  
  # A function without a name is called an anonymous function. And this syntax is called a lambda expression...
  def name(arguments):
    return expression
  
  # The following example uses the lambda expression to sort the companies by revenue from low to high
  companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

  # sort the companies by revenue
  companies.sort(key=lambda company: company[2])

  # show the sorted companies
  print(companies)    # Output: [('Apple', 2019, 260.2), ('Google', 2019, 134.81), ('Facebook', 2019, 70.7)]
    
  
