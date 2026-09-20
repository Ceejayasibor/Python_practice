# Function to taking in  a list of numbers and target number and return a list with two indices that add up to that number
#O(n²) time and O(1) space

def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum([1,4,8,22,5,6,11], 19))

def two_sum(nums: list[int], target: int) -> list[int]:
    for num in nums:
        complement = target - num
        if complement in nums and complement != num:
            return[nums.index(num), nums.index(complement)]
    return []

print(two_sum([1,4,8,22,5,6,11], 19))

def two_sum(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        for j, complement in enumerate(nums):
            if target == num + complement and num !=complement:
                return [i,j]
    return[]
        

print(two_sum([1,4,8,22,5,6,11], 19))


def two_sum(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        for j, complement in enumerate(nums):
            if complement == target - num and complement != num:
                return[i,j]
    return[]
        

print(two_sum([1,4,8,22,5,6,11], 19))


#Hash Map implementation
#HashMap implementation of twoSum, O(n) time, O(n) space

from typing import List


def two_sum(nums: list[int], target: int) -> list[int]:
    numsMap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in numsMap:
            return [numsMap[complement], i]
        #numsMap.update({nums[i]: i})
        numsMap[nums[i]]= i
    return[]
        
print(two_sum([1,4,8,22,5,6,11], 19))



def two_sum(nums: list[int], target: int) -> list[int]:
    numsMap ={}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numsMap:
            return [numsMap[complement], i]
        numsMap[num] = i
    return[]

print(two_sum([1,4,8,22,5,6,11], 19))

#Two_Sum for a sorted list of numbers
#Two pinters solution for two_sum_sorted: O(n) time, O(1) space
def two_sum_sorted(nums: List[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return[left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return[]



print(two_sum_sorted([1,4,5,6,8,11,22], 19))
