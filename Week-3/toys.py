'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    b = a + 1
    print(b)


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    b = a + 1
    return b # hint this is incomplete


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    c = a + b
    return c


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    c = sum(a, b)
    return(inc_return(c))


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    return a % 2 == 0


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    final_phrase = ''
    for x in range(repeat):
        final_phrase += phrase
    # hint: you can add strings together 
    # in order to concatenate them
    return final_phrase

