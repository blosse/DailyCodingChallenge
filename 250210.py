# Implement division of two positive integers without
# using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.

def div(x: int, y: int) -> int: # x / y

    if (y == 0):
        return ZeroDivisionError

    quotient: int = 0
    sum: int = y

    while sum <= x:
        sum = sum + y
        quotient = quotient + 1

    return quotient


### Test ###

assert (1 // 1) == div(1,1), f"Error {div(1,1)}"
assert (5 // 2) == div(5,2), f"Error {div(5,2)}"
assert (549095403985 // 98743298) == div(549095403985,98743298), f"Error {div(549095403985,98743298)}"
assert ZeroDivisionError == div(1,0), f"Error {div(1,0)}"
assert (1 // 2) == div(1,2), f"Error {div(1,2)}"

print("No issues, seems to work!")
