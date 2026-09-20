#inf and -inf will not work alone in python- NameError, without importing.- from math import inf, you can the use inf and -inf directly.
#float('inf') and float('-inf') always works without imports because the string - 'inf' is a special value float() recognizes.

#Maximum susbarray(no length restriction)  with the largest sum, return the sum.
#Time Complexity = O(n), Space Complexity =  O(1)
class Solution1():
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return "Empty array"
        
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)

        return max_sum
    
print(Solution1().maxSubArray([4,2,7,-4,6,-2,1,-3,5]))



#Time complexity = O(nlogn), Space complexity = O(log n).
class Solution2():
    def maxSubArray(self, nums):
        if not nums:
            return 0
        
        def helper(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_max = helper(left, mid)
            right_max = helper(mid + 1, right)

            # max crossing sum
            left_sum = float('-inf')
            s = 0
            for i in range(mid, left - 1, -1):
                s += nums[i]
                left_sum = max(left_sum, s)

            right_sum = float('-inf')
            s = 0
            for i in range(mid + 1, right + 1):
                s += nums[i]
                right_sum = max(right_sum, s)

            cross_max = left_sum + right_sum

            return max(left_max, right_max, cross_max)
        return helper(0, len(nums) - 1)

print(Solution2().maxSubArray([4,2,7,-4,6,-2,1,-3,5]))


'''Given an array of integers, return the maximum sum of any contiguous subarray of length EXACTLY k.'''
#Sliding window
#Time complexity is O(N), space is O(1)
def max_subarray_sum_exactly_k(nums, k):
    n = len(nums)
    if n < k:
        return "Array size is less than k."
    
    window_sum = sum[nums[:k]]
    max_sum = window_sum

    for i in range(k, n):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


'''Given an array of integers, return the maximum sum of any contiguous subarray of length at LEAST k.'''
#Prefix sum + running min
#Time complexity is O(N), Space is O(N)

def max_subarray_at_least_k(nums, k):
    n = len(nums)
    if n < k:
        return 'No subarray with length k or more.'
    

    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i]+ nums[i]

    min_prefix = float('inf') #or min_prefix = 0 because prefix[j-k] = 0, so both are same  and prefix[j] - 0 = prefix[j]
    max_sum = float('-inf')    #or max_sum, first valid sum satisfying at keleast k, correct answer still converges at the end


    #k = 3, n =6, n+1 = 7
    #let l ,j, be starting and ending indices that satisfy at least k length i.e. j-l >= k; l<=j-k, therefore left boundary must be from 0 to j-k
    for j in range(k, n+1): #j is right boundary which goes from k till end of prefix array- 3,4,5,6.
        min_prefix = min(min_prefix, prefix[j-k]) #j-k gives left boundary which varies from 0 to n-k: 0,1,2,3
        max_sum = max(max_sum, prefix[j] - min_prefix)
        '''for r in range(k, n+1):
              for l in range(0, r-k+1):
              max_sum = max(max_sum, prefix[r] - prefix[l])'''
    
    return max_sum




def max_subarray_atl_least_k(nums, k):
    n = len(nums)
    if n <k:
        return "No substring  of length k or more"
    
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    min_prefix = float('inf') #or min_prefix = 0 because prefix[j-k] = 0, so both are same  and prefix[j] - 0 = prefix[j]
    max_sum = float('-inf') #or max_sum, first valid sum satisfying at keleast k, correct answer still converges at the end
    for j in range(k, n+1):
        min_prefix = min(min_prefix, prefix[j-k])
        max_sum = max(max_sum, prefix[j] -  min_prefix)
    
    return max_sum


'''Given an array of integers, return the maximum sum of any contiguous subarray of length at MOST k.'''
#deque- double ended queue
#Time complexity is O(N) , space is O(N)
#Prefix sum + Monotonic increasing deque
from collections import deque
def subarray_max_at_most_k(nums, k):
    n = len(nums)
    if n == 0:
        return 0
    
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    '''for num in nums:
            prefix.append(prefix[-1] + num)'''

    dq = deque()
    max_sum = float('-inf')

    for j in range(len(prefix)): #iterate from j=0 and not j=1, so we don't miss subarrays starting from j=0.
        while dq and dq[0] < j-k:   #j-i<=k; i>=j-k
            dq.popleft()        #popleft to remove invalid indices from the front, as this would be the oldest/farthest indices no longer satisfying the criterion i>=j-k as we iiterate over j
        
        if dq:
            curr_sum = prefix[j] -prefix[dq[0]]
            max_sum = max(curr_sum, max_sum)


        while dq and prefix[dq[-1]] >= prefix[j]:  #keep monotonic increasing deque, only pop prefix indices whose prefixes are greater than the one to be added j, so thatprefix[dq[0]] can be minim to get max_sum
            dq.pop()


        dq.append(j)


    return max_sum


"""To get the minimum subarray sum for exactly, at least, at most, any k=length k, change all the max_sum =max() to min_sum = min()
Also change min_prefix to max_prefix as max_prefix gives min_sum, also note when intializing min_sum = float('inf') not -inf.
For at most k length, it has to be a monotonic decreasing order as you want the max at dq[0] hence dq.pop() when prefix[dq[--1]] <= pprefix[j]
"""



"""Max Subarray average where subarray length is exaxtly k"""
def max_subarray_average_exactly_length_k(nums, k):
    n = len(nums)
    if n < k:
        return "No subarray is up to length k."
    
    window_sum = sum[nums[:k]]
    max_sum = curr_sum

    for i in range(k, n):
        window_sum += nums[i] + nums[i-k]
        max_sum = max(max_sum, window_sum)

    max_average_length_k_subarray = max_sum/k

    return max_average_length_k_subarray

#Apply the same thing for minimum subarray average of exactly lenhgth k


'''Max/Min Product subarray any length'''
def max_product_Subarray(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]

    for x in range(1, len(nums)):
        x = nums[i]

        values = (x, x*curr_max, x*curr_min) #Negative values distort max and min products.

        curr_max = max(values)
        curr_min = min(values)

        max_prod = max(curr_max, max_prod)
        min_prod = min(curr_min, min_prod)
    
    return max_prod, min_prod

