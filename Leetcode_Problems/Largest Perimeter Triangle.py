# Largest Perimeter Triangle

''' Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, 
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, 
return 0.'''

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort the array in descending order
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0
            
sol = Solution()
nums = [2,1,2]
result = sol.largestPerimeter(nums)
print("Result:", result)