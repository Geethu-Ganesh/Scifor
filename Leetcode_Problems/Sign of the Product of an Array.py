# Sign of the Product of an Array

''' There is a function signFunc(x) that returns:
1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product)'''

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for num in nums:
            if num == 0:
                return 0
            product *= (1 if num > 0 else -1)
        
        return 1 if product > 0 else -1
        
sol = Solution()
nums = [-1,-2,-3,-4,3,2,1]
result = sol.arraySign(nums)
print("Result:", result)