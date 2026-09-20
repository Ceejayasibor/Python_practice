def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
    return nums, i+1

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))

def removeDuplicates(nums: list[int]) -> list[int]:
    if not nums:
        return 0
    i, j = 0,1
    while j < (len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
            j+=1
        else:
            j+=1
    return nums, i+1

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
    return nums, i

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
    return nums, i+1

nums = [1, 1, 1, 2, 2, 2, 3, 4, 4]
print(removeDuplicates(nums))



