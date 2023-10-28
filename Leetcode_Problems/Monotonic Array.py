# Monotonic Array

''' An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone 
decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.'''

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
            if nums[i] > nums[i - 1]:
                decreasing = False

        return increasing or decreasing

    
sol = Solution()
nums = [1,2,2,3]
result = sol.isMonotonic(nums)
print("Result:", result)