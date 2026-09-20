class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i]+=1
                return digits
            digits[i] = 0
        return [i] + digits
    

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s//10
        if carry:
            return [1] + digits
        return digits

