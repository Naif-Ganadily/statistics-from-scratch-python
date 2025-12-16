# TODO

# First Attempt:
"""
def mean(x):
    if len(x) == 0:
       raise ValueError("Cannot compute the mean due to an empty list")
    total = 0
    for num in x:
        total = total + num
    return total / len(x)
print("Mean of the List is ", mean(x))
"""

# First attempt is fine..... but lets make it better !!! 

# More Pythondic
# Second Attempt:
"""
def mean(x):
      if not x:
            raise ValueError("Cannot compute mean of empty list")
      total = 0
      for num in x:
            total += num
      return total / len(x)

print("Mean of the first list (x): ", mean(x))
print("Mean of the second list (y): ", mean(y))
print("Mean of the third list (z): ", mean(z))
"""
# Results of the second attempt is that it looks better more Pythondic approach
# However it doesnt check if all the elements are numerical or not 
# Lets add that using TypeError in the third attempt

# Third Attempt
# https://discuss.python.org/t/best-practice-for-type-checking-and-assert-statement/33728/5
# https://typing.python.org/en/latest/reference/best_practices.html
def mean(x):
    if not x: raise ValueError("Empty list")
    total = 0
    for num in x:
        try:
            total += num
        except TypeError:
            raise TypeError("Non-numeric: " + str(num))
    return total / len(x)

"""
print("Mean of the first list (x): ", mean(x))
print("Mean of the second list (y): ", mean(y))
print("Mean of the third list (z): ", mean(z))
"""