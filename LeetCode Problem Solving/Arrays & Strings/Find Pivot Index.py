# calculate the pivot index of an array
# given array of integers
# sum of nums left of pivot index = sum of nums right of pivot index
# pivots = 0 or len(array) - 1, represent pivots along the edges of array i.e. nums = [2,1,-1] pivot = 0 as nothing is left of 2, and nums[1] + nums[2] = 1 + (-1) = 0
# if no position exists whereby the LHS = RHS, pivot index = -1
# ---> nums = [1,2,3] -> Pivot = -1
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
import math


def pivotIndex(nums: [int]) -> int:

    pivot = -1

    # Though the approach below works we need something that has less time complexity. The below approach takes 63 ms, but falls short of all test cases, specifically the longer sets.
    '''
    n = len(nums)
    for i in range(n):

        leftSum, rightSum = 0, 0
        print("----------\nIteration: " + str(i))

        for x in range(n):
            if x < i:
                leftSum += nums[x]
            else:
                rightSum += nums[x]

        print("Left sum is: " + str(leftSum))
        print("Right sum is: " + str(rightSum))

        if leftSum == rightSum - nums[i]:
            return i
            break
    '''
    # alternate approach, time complexity = 141 ms for all cases
    leftSum = 0
    rightSum = sum(nums)

    for count, num in enumerate(nums):
        if leftSum == rightSum - leftSum - num:
            return count
        leftSum += num

    return pivot

print(pivotIndex([2,1,-1]))