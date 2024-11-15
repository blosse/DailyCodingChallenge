# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def solution (nums: list[int], k: int) -> bool:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == k):
                return True
    return False

# Test cases
case1 = [10, 15, 3, 7]
k1 = 17 # True
case2 = [17, 5, 39, 700000000000003333333]
k2 = 2 # False
case3 = [-9999, 15, 3, 7]
k3 = -9996 # True
case4 = [0] # False
k4 = -1

print("case 1:", solution(case1, k1))
print("case 2:", solution(case2, k2))
print("case 3:", solution(case3, k3))
print("case 4:", solution(case4, k4))
