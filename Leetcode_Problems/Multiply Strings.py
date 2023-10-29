# Multiply Strings

''' Given two non-negative integers num1 and num2 represented as strings, return the product of num1 
and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        num1 = [int(digit) for digit in num1][::-1]
        num2 = [int(digit) for digit in num2][::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += num1[i] * num2[j]
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result = [str(digit) for digit in result][::-1]

        return ''.join(result)

sol = Solution()
num1 = "2"
num2 = "3"
result = sol.multiply(num1,num2)
print("Result:", result)
            