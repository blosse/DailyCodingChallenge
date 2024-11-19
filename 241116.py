# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the # original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected # output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

# TODO create solution without division...

def solution(nums: list[int]) -> list[int]:
    sum = 1
    result = nums
    for i in range(len(nums)):
        sum *= nums[i]
    for i in range(len(nums)):
        if nums[i] == 0:
            result[i] = 0
        else:
            result[i] = (int) (sum / nums[i])
    return result

# Test cases
case1 = [1, 2, 3, 4, 5]
sol1 = [120, 60, 40, 30, 24]
case2 = [3, 2, 1]
sol2 = [2, 3, 6]
case3 = [0]
sol3 = [0]

# Run tests
print("Case 1:", solution(case1) == sol1)
print("Case 2:", solution(case2) == sol2)
print("Case 3:", solution(case3) == sol3)
