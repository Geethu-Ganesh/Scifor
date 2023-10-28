# Plus One

''' You are given a large integer represented as an integer array digits, where each digits[i] is the 
i-th digit of the integer. The digits are ordered from most significant to least significant in 
left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
            
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits.insert(0, carry)
        return digits

sol = Solution()
digits = [1,2,3]
result = sol.plusOne(digits)
print("Result:", result)