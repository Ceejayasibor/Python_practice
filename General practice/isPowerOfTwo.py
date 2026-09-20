#Return true or false, if an integer is a power of 2.
#n is an integer so only +ve and -ve whole numbers, no fractions.
#Given n is an integer, and we consider 2 and not -2, n cannot be -ve and n cannot be a fraction.

#O(log n) time, O(1) space.
def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    i= 0
    while n>1:
        n/=2
        i+=1
    if n == 1:
        return True, i
    return False


n =8192
print(isPowerOfTwo(n))

#O(log n) time, O(logn) recursion stack space.
def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return True
    return isPowerOfTwo(n/2)

n =8192
print(isPowerOfTwo(n))


#O(1) time, O(1) space.
#Most elegant and uses unique binary representation of powers of 2, and the bitwise and function- &.
def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n-1) == 0)

n =8192
print(isPowerOfTwo(n))

