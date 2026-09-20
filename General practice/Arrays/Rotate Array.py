#Rotate Array
#Time complexity = O(n), Space complexity = o(n)
def rotateArray(nums: list[int], k: int)-> list[int]:
    n = len(nums)
    k%=n
    temp = [0] * n
    for i in  range(n):
        temp[(i+k)%n] = nums[i]
    nums[:] = temp
    return nums

print(rotateArray([1,2,3,4,5,6], 2))


#Time complexity = O(n*k), Space Complexity = O(1)
def rotateArray(nums: list[int], k: int)-> list[int]:
    n = len(nums)
    k%=n

    for i in range(k):
        last = nums[-1]

        for r in range(n-1, 0,-1):
            nums[r] = nums[r-1]
        nums[0] = last
    return nums

print(rotateArray([1,2,3,4,5,6], 2))



#Time complexity = O(n), Space Complexity = O(1)
#For right rotation i.e. [1,2,3,4,5,6] --> [5,6,1,2,3,4]
#Reverse entire array
#Reverse first k elements
#Reverse remaining n-k elements
def rotateArray(nums: list[int], k: int)-> list[int]:
    n = len(nums)
    k%=n

    def reverse(left, right):
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right-=1

    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)
    
    return nums

print(rotateArray([1,2,3,4,5,6], 2))

#For left rotation i.e. [1,2,3,4,5,6] --> [3,4,5,6,1,2]
#Reverse first k elements i.e reverse(0, k-1)
#Reverse remaining n-k elements i.e.  reverse(k, n-1)
#Reverse entire array i.e. revere(0, n-1)



def rotateArray(nums: list[int], k: int)-> list[int]:
    n = len(nums)
    k %=n

    count = 0

    for start in range(n):
        if count>=n:
            break
        
        current = start
        prev = nums[start]

        while True:
            next_idx = (current+k)%n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count+=1

            if start == current:
                break
    return nums


print(rotateArray([1,2,3,4,5,6], 2))
