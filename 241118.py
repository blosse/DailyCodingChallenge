# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give # 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

# This one was tricky, looked up solution on StackOverflow
# Two key ideas:
    # 1. If all numbers between 1 and totalNumberOfPositivValuesInArray(n) exist in the array, we then know that the smallest integer will b n+1
    # 2. use the array to do a sort of vector encoding, in order to track which

def solution(arr) :
    # 1. Partition the array
    pos = 0
    neg = len(arr)-1
    while pos < neg:
        if arr[neg] < 0:
            neg -= 1
        elif arr[pos] < 0:
            arr[neg], arr[pos] = arr[pos], arr[neg]
            neg -= 1
            pos += 1
        else:
            pos += 1
    end = pos + 1

    # 2.
    for i in range(end):
        if abs(arr[i]) < end:
            vectorIndex = abs(arr[i])
            if arr[vectorIndex-1] > 0:
                arr[vectorIndex-1] *= -1

    # 3.
    ret = 1
    for i in range(end-1):
        if arr[i] > 0:
            return i+1 # +2 is to compensate for zero indexing
        else:
            ret += 1

    return ret

# Test
case1 = [1, -1, -5, -3, 3, 4, 2, 8]
case2 = [3, 4, -1, 1]
case3 = [-2, 99, 99, 5, 8, -1]

result1 = solution(case1)
result2 = solution(case2)
result3 = solution(case3)

assert result1 == 5, f"Returned: {solution(case1)}"
assert result2 == 2, f"Returned: {solution(case2)}"
assert result3 == 1, f"Returned: {solution(case3)}"
