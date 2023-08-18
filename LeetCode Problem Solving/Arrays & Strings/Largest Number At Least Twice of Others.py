# Largest Number At Least Twice of Others
import math, array
'''
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.

2 <= nums.length <= 50
0 <= nums[i] <= 100
----> largest element in nums is unique
'''

def dominantIndex(nums: [int]) -> int:

    maxNums = [nums.index(max(nums)), nums.pop(nums.index(max(nums)))]

    if maxNums[1] >= 2 * max(nums):
        return maxNums[0]

    return -1

