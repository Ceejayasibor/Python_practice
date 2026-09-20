#Moving 0s to the end in-place without retaining the relative order of non-zero elements

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[j] == 0:
                j -= 1
            elif nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j-=1
            else:
                i +=1


nums1= [0,1,0,3,12]
solution1 = Solution()
solution1.moveZeroes(nums1)
print(nums1)

#Moving 0s to the end of the array while maintaining the relative order of elemments.
#Bubble sort method- time complexity: O(n²), Space complexity: O(1).

def moveZeros(nums: list) -> None:
    for i in range(len(nums)):
        for j in range(i, len(nums)-i-1):
            if nums[j] == 0:
                 nums[j+1], nums[j] = nums[j], nums[j+1]
    return  nums


nums1= [0,1,0,3,12]
print(moveZeros(nums1))
print(nums1)


#Bubble sort method- time complexity: O(n), Space complexity: O(1).

def moveZeros(nums: list[int]) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i] = nums[j]
            i+=1
    for k in range(i, len(nums)):
        nums[k] = 0

nums1= [0,1,0,3,12]
moveZeros(nums1)
print(nums1)


def moveZeros(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right]!= 0:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
    return nums

nums1= [0,1,0,3,12]
print(moveZeros(nums1))
print(nums1)









            