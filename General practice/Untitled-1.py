'''def isPalindrome(x: int) -> bool:
    y= str(x)
    if (x == y[::-1]):
        return True
    return False

x= 456
print(isPalindrome(x))'''


'''
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1




#Two_Pointers 1
#Two_Pointers for two_sum_sorted
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums)-1
    while left<right:
        current_sum = nums[left]+nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return []


#Two_Pointers 2
#Two_Pointers for in-place removing duplicates from a sorted string
def removeDuplicates(nums: list[int]) -> int:
    i = 0 
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
    return i+1, nums[:i+1]



import heapq
lst1 = [1,2,3,5,6,8]
lst2 = [2,3,4,5,7,9,10]
res1 = list(heapq.merge(lst1,lst2))
res2 = lst1 + lst2
print(res1, res2)


#Two_Pointers 3
#Two_Pointers for merging sorted array using new array, removing duplicates
def merge_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    i, j = 0, 0
    merg= []
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merg.append(nums1[i])
            i+=1
        elif nums2[j]<nums1[i]:
            merg.append(nums2[j])
            j+=1
        else:
            merg.append(nums1[i])
            i+=1
            j=+1
    return merg

nums1 = [1,2,3,5,6,8]
nums2 = [2,3,4,5,7,9,10]

print(merge_sorted_arrays(nums1, nums2))



'''

# ✅ VISUAL ROADMAP & PYTHON IMPLEMENTATIONS

# -------------------------------
# 📌 1. Insertion Sort (Beginner, Stable)
# -------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Dry Run Example:
# arr = [4, 3, 2, 1]
# i=1, key=3 -> [4,4,2,1] -> [3,4,2,1]
# i=2, key=2 -> [3,4,4,1] -> [3,3,4,1] -> [2,3,4,1]

# -------------------------------
# 📌 2. Merge Sort (Stable, Always O(n log n))
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Dry Run:
# [4,3,2,1] -> split into [4,3] and [2,1] -> merge to [3,4], [1,2] -> merge to [1,2,3,4]

# -------------------------------
# 📌 3. Quick Sort (In-Place, Fast Average Case)
# -------------------------------
def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr

# Dry Run: [4,3,2,1], pivot = 1 -> place 1 at start, recurse on [4,3,2]...

# -------------------------------
# 📌 4. Counting Sort (Non-comparison, Linear Time)
# -------------------------------
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    output = []
    for i, c in enumerate(count):
        output.extend([i] * c)
    return output

# Only works for non-negative integers in a small range

# -------------------------------
# 📌 5. Heap Sort (Always O(n log n), In-Place)
# -------------------------------
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


# ✅ TERMS
# -------------------------------
# Stable sort: Keeps the relative order of equal elements
#    E.g. [4a, 4b, 3] -> stable sort = [3, 4a, 4b]; unstable = [3, 4b, 4a]
# Consistent: Always has the same time complexity regardless of input (e.g., Merge Sort is always O(n log n))

# CP = Competitive Programming — timed coding challenges (e.g. Codeforces, AtCoder, Leetcode contests)


# 🔁 Let me know if you'd like visual animations or flowcharts for any of these.
