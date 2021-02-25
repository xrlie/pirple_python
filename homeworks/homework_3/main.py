# # # # # # # # # # # # # # # # # # # # # # # #
#    Homework Assignment #3: If statements    #
# # # # # # # # # # # # # # # # # # # # # # # #

"""
Create a function that accepts 3 parameters and
checks for equality between any two of them.

The function should return TRUE if 2 or more of
the parameters are equal and FALSE if none of them
are equal.

For extra credit, modify the function so that strings
can be compared to integers if they are equivalent.
"""

### Function definition

def compare_parameters(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False

### Extra credit

def compare_any(a, b, c):
    if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
        return True
    else:
        return False

### Evaluating each function

compare_parameters(1, 2, 3)     # False
compare_parameters(1, 3, 2/2)   # True
compare_parameters(1, 2, '2')   # False / Can't compare int with string

compare_any(1, 2, 3)            # False
compare_any(1, 4, 7/7)          # True
compare_any(1, 2, '2')          # True / I used the function int()
                                # that turns any string to an integer.