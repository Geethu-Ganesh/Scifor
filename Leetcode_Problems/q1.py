''' Merge two strings by adding letters in alternating order, If a string is longer than the other,
append the additional letters onto the end of the merged string.
'''

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        merged_list =[]

        i=0
        j=0
        while i<len(word1) and j<len(word2):
            merged_list.append(word1[i])
            merged_list.append(word2[j])
            i+=1
            j+=1
        
        while i < len(word1):
            merged_list.append(word1[i])
            i += 1

        
        while j < len(word2):
            merged_list.append(word2[j])
            j += 1


        return ''.join(merged_list)


sol=Solution()
word1= "abc"
word2= "pqr"
result=sol.mergeAlternately(word1,word2)
print("result",result)