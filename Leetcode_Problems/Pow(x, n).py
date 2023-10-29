# Pow(x, n)

''' Implement pow(x, n), which calculates x raised to the power n (i.e., xn).'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result

sol = Solution()
x = 2.00000
n = 10
result = sol.myPow(x,n)
print("Result:", result)