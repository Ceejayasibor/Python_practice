# Sort the list of numbers using Bubble Sort algorithm.
# Bubble Sort: time complexity: O(n²), Space complexity: O(1). Worst and average case time complexity is O(n²), and best case is O(n).
# Bubble Sort algorithm is implemented by constantly comparing each element to the next in a dataset and if greater, swapping in a pass until all elements are fully sorted.


def bubble_sort(nums: list) -> list:
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(len(nums)-i-1):    
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums [j+1], nums[j]
                #temp = nums[j]
                #nums[j] = nums[j+1]
                #nums[j+1] = temp
                swapped = True
        if not swapped:
            break
    return nums


nums = [51,14,37,12,12,10]
print(bubble_sort(nums))

#Insertion sort works by taking the first element sorted and going element by element and inserting each element at the right index in the already sorted left path.
#Time complexity is O(n²), space complexity is O(1). Worst and average case time complexity is O(n²), and best case is O(n).



def insertion_sort(nums: list[int]) -> None:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

nums= [2,6,5,1,3,3,4]
print(insertion_sort(nums))


def insertion_sort_with_swaps(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        j = i 
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j] # Swap
            j -= 1 

    return arr

arr= [2,6,5,1,3,3,4]
print(insertion_sort_with_swaps(arr))

def insertion_sort_with_swaps(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1] # Swap
            j -= 1 

    return arr

arr= [2,6,5,1,3,3,4]
print(insertion_sort_with_swaps(arr))



# Sort the list of numbers using Selection Sort algorithm.
# Selection Sort: time complexity: O(n²), Space complexity: O(1). Worst, average and best case time complelxity are all O(n²).
# Selection sort algorithm is implemented by constantly selecting the smallest element in a data set and placing it at the foremost indices from L to R accordingly till fully sorted.



# Selection sort option 1
def selection_sort(nums: list[int]) -> list[int]:
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
print(selection_sort(nums))

### 🔢 Sorting Algorithms - Summary with Stability, Space, and CP Friendliness
'''
| Algorithm       | Best Case   | Average Case | Worst Case   | Space | Stable? | In-Place? | CP Friendly? |
|----------------|-------------|--------------|--------------|-------|---------|-----------|---------------|
| **Bubble Sort**     | O(n)        | O(n²)        | O(n²)        | O(1)  | ✅ Yes  | ✅ Yes    | ❌ Rarely Used |
| **Insertion Sort**  | O(n)        | O(n²)        | O(n²)        | O(1)  | ✅ Yes  | ✅ Yes    | ✅ Sometimes   |
| **Selection Sort**  | O(n²)       | O(n²)        | O(n²)        | O(1)  | ❌ No   | ✅ Yes    | ❌ Rarely Used |
| **Merge Sort**      | O(n log n)  | O(n log n)   | O(n log n)   | O(n)  | ✅ Yes  | ❌ No     | ✅ Yes        |
| **Heap Sort**       | O(n log n)  | O(n log n)   | O(n log n)   | O(1)  | ❌ No   | ✅ Yes    | ✅ Sometimes   |
| **Quick Sort**      | O(n log n)  | O(n log n)   | O(n²)        | O(log n) | ❌ No | ✅ Yes    | ✅ Very Common |
| **Bucket Sort**     | O(n + k)    | O(n + k)     | O(n²)        | O(n)  | ✅ Yes  | ❌ No     | ✅ Niche Uses  |
| **Radix Sort**      | O(nk)       | O(nk)        | O(nk)        | O(n + k) | ✅ Yes | ❌ No   | ✅ Occasionally|
| **Counting Sort**   | O(n + k)    | O(n + k)     | O(n + k)     | O(k)  | ✅ Yes  | ❌ No     | ✅ Sometimes   |

'''