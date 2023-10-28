# To Lower Case

''' Given a string s, return the string after replacing every uppercase letter with the same lowercase 
letter.'''

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        lowercase_s = s.lower()
        return lowercase_s

sol = Solution()
s = "Hello"
result = sol.toLowerCase(s)
print("Result:", result)