# Length of Last Word

''' Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if len(words) == 0:
            return 0
        last_word = words[-1]
        return len(last_word)
        
sol = Solution()
s = "Hello World"
result = sol.lengthOfLastWord(s)
print("Result:", result)