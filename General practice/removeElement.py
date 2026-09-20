#Remove elements = value and return length of elements != value.
#Time Complexity O(n), Space complexity O(n), in-place.

def removeElement(nums: list[int], val: int) -> tuple[int, list[int]]:
    k = 0
    for i in range(len(nums)):
        if nums[i]!= val:
            nums[k], nums[i] = nums[i], nums[k]
            k +=1
    return k, nums[:k], nums

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))