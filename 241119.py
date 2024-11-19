# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:
def cons(a, b):
    # This function returns an object which accepts a function f.
    # When the object is called, the object will call the function f and pass parameters a and b to the function.
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.
#
# Had to google... Interesting problem tho
# https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python
#
# Solution:
def car(pair):
    def return_first(a, b):
        return a
    return pair(return_first)

def cdr(pair):
    def return_last(a,b):
        return b
    return pair(return_last)

# Test
assert car(cons(3,4)) == 3
assert cdr(cons(3,4)) == 4
