#Instead of keeping count for each elemenT, key is to compare each element in index i with the element in index i+2, since the array is sorted.
#Your for/while looop should always contain the condition where you do something and not just continue (control flow). Control flow: pass(placholder), continue(skip specific iteration), break(break the entire loop)
#Time complexity O(n), space complexity- O(1).

nums = [0,0,0,0,0,1,1,1,2,2,3,3,4]

class Solution:
  
    def removeDuplicates(self, nums:list[int]) -> int: 
        if len(nums) <=2 :
            return [len(nums), nums]
        n = len(nums)
        i = 0
        for j in range(2, n):
            if nums[i] != nums[j]:
                nums[i+2] = nums[j]
                i+=1   
        return [i+2, len(nums[:i+2]), nums[:i+2]]

class Solution1:
    def removeDuplicates1(self, nums):
        i,j = 0, 2
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+2] = nums[j]
                i+=1
            j+=1
        return [len(nums[:i+2]), nums[:i+2], nums]
 

class Solution2:
    def removeDuplicates2(self, nums:list[int]) -> int: 
        if len(nums) <=2 :
         return [len(nums)]
        n = len(nums)
        i = 2
        for j in range(2, n):
            if nums[i-2] != nums[j]:
                nums[i] = nums[j]
                i+=1   
        return [i,  nums[:i]]


class Solution3:
    def removeDuplicates3(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 2
        for j in range(2, len(nums)):
            if nums[k-2] != nums[j]:
                nums[k] = nums[j]
                k+=1
        return [k, nums[:k]]


print(Solution().removeDuplicates(nums.copy()))
print(Solution1().removeDuplicates1(nums.copy()))
print(Solution2().removeDuplicates2(nums.copy()))
print(Solution3().removeDuplicates3(nums.copy()))

#Problem statement, remove duplicates from a ssorted list, however, each elemt can have a macimum of 2 frequency.
#When comparing, need to check if an element has a 2nd occurence, only after 2nd occurrence, swap.