# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

# Idea: 
# If next number is larger than current number -> Pick next number and inc curr
# Else pick current number and inc curr twice
# Edge case: If next number is null, pick curr

def maxSumNonAdj(vals):
    sum = 0
    picks = []
    curr = 1
    
    # Empty list
    if len(vals) == 0:
        return (0, [])

    # Single element
    if len(vals) == 1:
        return (vals[0], [vals[0]]) 

    # Case where we want to pick third element
    if vals[curr] < vals[curr+1]:
        sum = vals[curr+1] + vals[0]
        picks.append(vals[0])
        picks.append(vals[curr+1])
        curr = curr + 2
    # Main logic
    while curr < len(vals) - 1:
        if vals[curr] >= vals[curr+1]:
            sum = sum + vals[curr]
            picks.append(vals[curr])
            curr = curr + 1
        else:
            sum = sum + vals[curr + 1]
            picks.append(vals[curr + 1])
            curr = curr + 2

    return sum, picks

### Test ###

test1 = [2, 4, 6, 2, 5]
ans1 = (13, [2, 6, 5])

test2 = [1, 1, 1, 5]
ans2 = (6, [1, 5])

test3 = [1]
ans3 = (1, [1])

test4 = []
ans4 = (0, [])

assert maxSumNonAdj(test1) == ans1, f"Test 1 returned: {maxSumNonAdj(test1)}"
assert maxSumNonAdj(test2) == ans2, f"Test 2 returned: {maxSumNonAdj(test2)}"
assert maxSumNonAdj(test3) == ans3, f"Test 3 returned: {maxSumNonAdj(test3)}"
assert maxSumNonAdj(test4) == ans4, f"Test 4 returned: {maxSumNonAdj(test4)}"
