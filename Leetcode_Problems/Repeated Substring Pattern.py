# Repeated Substring Pattern

''' Given a string s, check if it can be constructed by taking a substring of it and appending multiple 
copies of the substring together.'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        n = len(s)
        for i in range(1, n):
            if n % i == 0:
                substring = s[:i]
                multiple_substring = substring * (n // i)

                if multiple_substring == s:
                    return True

        return False

sol = Solution()
s = "abab"
result = sol.repeatedSubstringPattern(s)
print("Result:", result)
