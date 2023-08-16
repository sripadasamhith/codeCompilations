import math

# input a list with 1 to 30,000 integers
# integers between [-100, 100]
# sorted in ascending order
    # first int is smallest and last is largest

'''
The implementation below won't work because the question asks us to not use any space thereby asking us to manipulate the original array.

nums = input()
smallNum = nums[0]
largeNum = nums[len(nums) - 1]

def removeDuplicates(nums: [int]) -> int:

    uniqueNums = []

    for i in range(smallNum, largeNum + 1):
        if i in nums:
            uniqueNums.append(i)

    return uniqueNums

print(removeDuplicates(nums))
'''
def removeDuplicates(nums: [int]) -> int:

    length = len(nums)
    startIndex = 1

    for i in range(1, length):
        # found the unique integer
        if nums[i - 1] != nums[i]:
            nums[startIndex] = nums[i]
            startIndex += 1
    return startIndex


















