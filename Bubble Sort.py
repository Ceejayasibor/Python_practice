# Sort the list of numbers using Bubble Sort algorithm.
# Bubble Sort: time complexity: O(n²), Space complexity: O(1)
# Bubble Sort algorithm is implemented by constantly comparing each element to the next in a dataset and if greater, swapping in a pass until all elements are fully sorted.

'''
def bubble_sort(nums: list) -> list:
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(len(nums)-i-1):    
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums [j+1], nums[j]
                #temp = nums[j]
                #nums[j] = nums[j+1]
                #nums[j+1] = temp
        if not swapped:
            break
    return nums


nums = [51,14,37,12,12,10]
print(bubble_sort(nums))
'''


# Sort the list of numbers using Selection Sort algorithm.
# Selection Sort: time complexity: O(n²), Space complexity: O(1)
# Selection sort algorithm is implemented by constantly selecting the smallest element in a data set and placing it at the foremost indices from L to R accordingly till fully sorted.



# Selection sort option 1
'''def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            min_value = min(nums[i:])
            min_index= nums.index(min_value, i)
            if min_index != i:
            #if min_value < nums[i]:
                nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


nums = [51,14,37,12,12,10]
print(selection_sort(nums))

nums = [51,14,37,12,10]
print(selection_sort(nums))


#Selection sort Option 2
def selection_sort(nums: list[int]) -> list[nums]:
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

nums = [51,14,37,12,12,10]
print(selection_sort(nums))

nums = [51,14,37,12,10]
print(selection_sort(nums))'''

#Insertion sort wrks by taking the first element sorted and oing element by elemt and inserting each element at the right index is the already sorted left path.

def insertion_sort(nums: list[int]) -> None:
    for i in range(1, len(nums)): #Leftmost element already sorted, traversing other elementa one by one from L to R.
        print(f'Original nums: {nums}, =end', '')
        print(f'i = {i}')
        key = nums[i] #element we want to insert in sorted portion
        print(f'key=nums[{i}] = {nums[i]}')
        j = i - 1 #Already sorted region
        print(f'j={i-1}')
        while j>=0 and key<nums[j]: #j >=0 so we don't run out of index and element we want to innsert is less than the sorted element
            nums[j+1]=nums[j]
            print(f'{nums}')
            j-=1
            print(f'{j}')
        nums[j+1] = key
        print(f'{nums}')
    return nums


nums= [2,6,5,1,3,3,4]
print(insertion_sort(nums))

'''
def insertion_sort(nums: list[int]) -> None:
    for i in range(1, len(nums)): #Leftmost element already sorted, traversing other elementa one by one from L to R.
        #key = nums[i] #element we want to insert in sorted portion
        j = i - 1 #Already sorted region
        while j>=0 and nums[i]<nums[j]: #j >=0 so we don't run out of index and element we want to innsert is less than the sorted element
            nums[j], nums[i]=nums[i], nums[j]
            j-=1
      
    return nums

nums= [2,6,5,1,3,3,4]
print(insertion_sort(nums))
'''
