# Count Odd Numbers in an Interval Range

''' Given two non-negative integers low and high. Return the count of odd numbers between low and 
high (inclusive).'''

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 == 0:
            low += 1

        if high % 2 == 0:
            high -= 1

        count = (high - low) // 2 + 1
        return count

sol = Solution()
low = 3
high = 7
result = sol.countOdds(low, high)
print("Result:", result)