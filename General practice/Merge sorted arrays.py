#Merge sorted arrays
#O(m+n) time and O(1) space
def merge(nums1: list[int], m: int, nums2: list[int], n: int) ->None:
    i = m - 1
    j = n - 1
    k = m + n -1
    while j >= 0:
        if i >=0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -=1
        else: 
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

nums1 = [1,3,4,0,0,0]
nums2 = [2,2,3]
m= 3
n= 3
solution = merge(nums1, m, nums2, n)
print(nums1)

# o(m+n) time and O(1) space.
def merge(nums1: list[int], m: int, nums2: list[int], n: int) ->None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else: 
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >=0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1 = [1,3,4,0,0,0]
nums2 = [2,2,3]
m= 3
n= 3
solution = merge(nums1, m, nums2, n)
print(nums1)