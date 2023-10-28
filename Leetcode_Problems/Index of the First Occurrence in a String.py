# Index of the First Occurrence in a String

''' Given two strings needle and haystack, return the index of the first occurrence of needle in 
haystack, or -1 if needle is not part of haystack.'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        needle_length =len(needle)
        for i in range(len(haystack) - needle_length+1):
            if haystack[i:i + needle_length] == needle:
                return i


        return -1

sol = Solution()
haystack = "sadbutsad"
needle = "sad"
result = sol.strStr(haystack, needle)
print("Result:", result)