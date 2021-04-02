# # # # # # # # # # # # # # # # # # # #
#    Homework Assignment #4: Lists    #
# # # # # # # # # # # # # # # # # # # #

"""
Create a a global variable called myUniqueList. It
should be an empty list to start.

Next, create a function that allows you to add things
to that list. Anything that's passed to this function
should get added to myUniqueList, unless its value
already exists in myUniqueList. If the value doesn't 
exist already, it should be added and the function
should return true. If the value does exist, it should
not be added, and the function should return false.

Finally, add some code below your function that tests
it out. It should add a few different elements, showcasing 
the different scenarios, and then finally it should print 
the value of myUniqueList to show that it worked.

For extra credit, add another function that pushes all the 
rejected inputs into a separate global array called myLeftovers. 
If someone tries to add a value to myUniqueList but it's rejected 
(for non-uniqueness), it should get added to myLeftovers instead.
"""

### Global variables

my_unique_list = []
my_leftovers = []

### Function definition

def add_things_2list(anything):
    if my_unique_list.count(anything):
        return False
    else:
        my_unique_list.append(anything)
        return True

### Testing add_things_2list
add_things_2list('Hello')               # Adds 'Hello' to my_unique_list and returns True
add_things_2list('World')               # Adds 'World' to my_unique_list and returns True
add_things_2list(10)                    # Adds 10 to my_unique_list and returns True
add_things_2list(16)                    # Adds 16 to my_unique_list and returns True
add_things_2list('Hello')               # Doesn't add 'Hello' to my_unique_list and returns False
add_things_2list(True)                  # Adds True to my_unique_list and returns True
add_things_2list(False)                 # Adds False to my_unique_list and returns True
add_things_2list([1,3,5,7,9])           # Adds [1,3,5,7,9] to my_unique_list and returns True
add_things_2list(16)                    # Doesn't add 16 to my_unique_list and returns False
add_things_2list({'Hello':'World'})     # Adds {'Hello':'World'} to my_unique_list and returns True
print(my_unique_list)                   # Prints my_unique_list as follows 
                                        # -> ['Hello', 'World', 10, 16, True, False, [1,3,5,7,9], {'Hello':'World'}]


### Extra credit

def add_2list(anything) :
    my_leftovers.append(anything) if my_unique_list.count(anything) else my_unique_list.append(anything)
    return print(my_unique_list, '\n', my_leftovers)

### Testing extra credit function

add_2list('Hello')                  
# Since 'Hello' is already in my_unique_list (from previous testing)
# It will be added to my_leftovers.
# The result will be
# -> ['Hello', 'World', 10, 16, True, False, [1,3,5,7,9], {'Hello':'World'}]
#    ['Hello'] 

add_2list(True)
# Since True is already in my_unique_list (from previous testing)
# It will be added to my_leftovers.
# The result will be
# -> ['Hello', 'World', 10, 16, True, False, [1,3,5,7,9], {'Hello':'World'}]
#    ['Hello', True]

add_2list([2,4,6,8])
# Since [2,4,6,8] is not in my_unique_list (from previous testing)
# It will be added to my_unique_list.
# The result will be
# -> ['Hello', 'World', 10, 16, True, False, [1,3,5,7,9], {'Hello':'World'}, [2,4,6,8]]
#    ['Hello', True]