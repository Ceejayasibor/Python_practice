#Remove duplicates from a sorted listed of numbers.
#Can't use a for loop here when popping, because the range of the for loop is defined at the start, if you pop any element, you'll get out of range. Better to use while i < len(nums) -1


#O(N) Time complexity, all elements inside the for loop are O(1) x N, O(1) space complexity.
def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i +=1
            nums[i]=nums[j]
    return i+1, nums[:i+1]

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))

#Using while loop.
#Key point using while loop, increment read pointer i.e. j once, if you use if/else, increment j in both, using only if, increment j outside if to prevent skipping an index.
def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    i, j = 0,1
    while j < (len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
        j+=1
    return i+1, nums[:i+1]

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))

def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    i, j = 1, 0
    while j < (len(nums)) - 1:
        if nums[j] != nums[j+1]:
            j+=1
            nums[i] = nums[j]
            i+=1
        else:
            j+=1
    return i, nums[:i]

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))


def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    i, j = 0, 0
    while j < (len(nums)) - 1:
        if nums[j] != nums[j+1]:
            j+=1
            i+=1
            nums[i] = nums[j]
        else:
            j+=1
    return i+1, nums[:i+1]

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))


# O(N²) time complexity as worst case scenario [1,1,1,1,1...] One pop is o(n) as you have to shift elemnts, times n-1 times, space complexisty isO(1). Can't use op with for loop as range of loop is predefined and pop shrinks range.
def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i+1) #Pop is O(N), after a Pop, you need to shift all elements (n-1) so that the elements are contiguous in memory
        else:
            i+=1
    return len(nums), nums

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))




#O(N)-->O(N)+O(N) time complexity, O(N)-->O(N)+O(N) space complexity. 
def removeDuplicates(nums: list[int]) -> list[int]:
    nums = set(nums)
    nums= list(nums)
    return len(nums), nums

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))
                


#Remove duplicates when the list is sorted (not in place)
#O(N²) time complexity, In check is O(N), performend over (N) times for len(nums), O(N) space
def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    no_duplicates =[]
    for i in range(len(nums)):
        if nums[i] not in no_duplicates:
            no_duplicates.append(nums[i])
    return len(no_duplicates), no_duplicates

nums = [4,2,3,1,3,2,5,4,2,1,1,4]
print(removeDuplicates(nums))


def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    no_duplicates =[]
    i = 0
    while i < len(nums):
        if nums[i] not in no_duplicates:
            no_duplicates.append(nums[i])
        i+=1
    return len(no_duplicates), no_duplicates

nums = [4,2,3,1,3,2,5,4,2,1,1,4]
print(removeDuplicates(nums))

#O(N²) time complexity, In check is O(N) in no_duplicates + Pop- (N) over (N) times for original nums, O(N) space
def removeDuplicates(nums: list[int]) -> list[int]:
    no_duplicates = []
    i = 0
    while i < len(nums):
        if nums[i] in no_duplicates:
            nums.pop(i)
        else:
            no_duplicates.append(nums[i])
            i+=1
    return nums, no_duplicates

nums = [4,2,3,1,3,2,5,4,2,1,1,4]
print(removeDuplicates(nums))





def removeDuplicatesSortedArray(nums: list[int]) ->int:
    if not nums:
        return 0
    seen = {}
    i=0
    while i < len(nums):
        if nums[i] not in seen:
            seen[nums[i]] = i
        i+=1
    return (seen, len(seen))

nums = [4,2,3,1,3,2,5,4,2,1,1,4]
print(removeDuplicates(nums))

'''
If list is unsorted, use list.sort which is O(NlogN) then apply two pointers to remove duplicates, O(NlogN) +O(N)- for loop and constant items within gives O(NLogN) time, 
O(1) for space is list.sort uses in-place sort like Heapsort, could be O(N) worst case for auxiliary sorting.
Option two- use set but not in place.
'''
#O(N3) time complexity, O(1) space.
class Solution:
    def removeDuplicatesUnsortedBruteForce(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0 # Pointer for the current unique element
        while i < len(nums) -1:
            j = i + 1 # Pointer to compare against nums[i]
            while j < len(nums):
                if nums[j] == nums[i]:
                    nums.pop(j) # O(N) operation, shifts elements
                else:
                    j += 1 # Only advance j if no element was popped
            i += 1 # Move to the next element to consider as unique
        
        return len(nums)
        









