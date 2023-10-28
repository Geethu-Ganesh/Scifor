# Valid Anagram

''' Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sort1 = sorted(s)
        sort2 = sorted(t)

        return sort1 == sort2

sol = Solution()
s = "anagram"
t = "nagaram"
result = sol.isAnagram(s, t)
print("Result:", result)