# Make Arithmetic Progression From Sequence

''' A sequence of numbers is called an arithmetic progression if the difference between any two 
consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic 
progression. Otherwise, return false.'''

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        common_diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != common_diff:
                return False
        
        return True

sol = Solution()
arr = [3,5,1]
result = sol.canMakeArithmeticProgression(arr)
print("Result:", result)