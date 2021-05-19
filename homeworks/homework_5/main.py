# # # # # # # # # # # # # # # # # # # # # # #
#    Homework Assignment #5: Basic Loops    #
# # # # # # # # # # # # # # # # # # # # # # #

"""
You're about to do an assignment called "Fizz Buzz", which is one of the 
classic programming challenges. It is a favorite for interviewers, and a 
shocking number of job-applicants can't get it right. But you won't be one
of those people. Here are the rules for the assignment (as specified by 
Imran Gory):

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and
for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

For extra credit, instead of only printing "fizz", "buzz", and "fizzbuzz", 
add a fourth print statement: "prime". You should print this whenever you 
encounter a number that is prime (divisible only by itself and one). 
As you implement this, don't worry about the efficiency of the algorithm 
you use to check for primes. It's okay for it to be slow.
"""

# First part of the homework:
# I used a for to print all the numbers from 1 to 100
for number in range(1,101):
  # First we check if the number is divisible by 3 and 5
  if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
  # Second, if the previous condition wasn't fulfilled, we check if it is only divisible by 3
  elif number % 3 == 0:
    print("Fizz")
  # Third, if the previous condition wasn't fulfilled, we check if it is only divisible by 5
  elif number % 5 == 0:
    print("Buzz")
  # Fourth, if none of the previous condition was fulfilled, then we just print the number.
  else:
    print(number)

### Extra credit

# I define a function to check if the number is prime or not comparing it with the first 100 numbers
def is_prime(number):
  counter = 0
  for divisor in range (1,101):
    if counter == 3:
      break
    else:
      if number >= divisor :
        if number % divisor == 0:
          counter += 1
        else:
          continue
      else:
        continue
  if counter == 1 or counter == 3:
    return False
  else:
    return True

# Then I use the same code from the first part of this homework just that I add the new function in the loop.
for number in range(1,101):
  if is_prime(number):
    print("prime")
  else:
    if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
    elif number % 3 == 0:
      print("Fizz")
    elif number % 5 == 0:
      print("Buzz")
    else:
      print(number)