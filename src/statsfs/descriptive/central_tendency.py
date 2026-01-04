# TODO

### First Attempt at the Mean Function:
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


### First Attempt at the Median Function:
# It’s straightforward: we need the middle number of a list.
# We’re focusing on 1D data for now...... nothing too complex..... YET ;)

# Median means: the value with half the data below it and half above it.

# Step 1: The list needs to be sorted (so we need a sorting algorithm / sorting step).
# Step 2: Count the length of the list and call it (n).
# Step 3: If (n) is an odd number, the median position (in human counting) is (n + 1) / 2.
# Step 4: If (n) is an even number, the middle positions are n/2 and (n/2) + 1.
# Step 5: Add the two middle values and take the average (divide by 2).
#
# Notes:
# - If the number of elements is even, we take the sum of the two middle elements and divide by 2.
# - The list can’t be empty.
# - The list must contain only numerical values.

"""
def median(x):
    if not x: raise ValueError("Empty List")
    for i in x:
        if not isinstance(i, (int, float)):
            raise TypeError(f"Non-numeric: {i}")
    nums = sorted(x)
    n = len(nums)
    middle = n // 2
    if n % 2 == 1:
        return nums[middle]
    else:
        return (nums[middle - 1] + nums[middle]) / 2
"""

        
# isinstance(i, (int, float)) checks whether i is a number (int or float)
# If it isn’t stop the function and raise a TypeError
# The rest follows the formula 



# Second Attempt:    
# More Pythondic
    
def median(x):
    if not x: raise ValueError("Empty List")
    for i in x:
        if not isinstance(i, (int, float)):
            raise TypeError(f"Non-numeric: {i}")
    nums = sorted(x)
    n = len(nums)
    middle = n // 2
    return nums[middle] if n % 2 else (nums[middle - 1] + nums[middle]) / 2

# First attempt on the Midrange Feature 
# Works !
def midrange(x):
    if not x: raise ValueError("Empty List")
    for i in x:
        if not isinstance(i, (int, float)):
            raise TypeError(f"Non-numeric: {i}")
    return (max(x) + min(x)) / 2