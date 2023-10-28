# Matrix Diagonal Sum

''' Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary 
diagonal that are not part of the primary diagonal.'''

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        primary_sum = 0
        secondary_sum = 0
        
        for i in range(n):
            primary_sum += mat[i][i]
            secondary_sum += mat[i][n - i - 1]
        
        return primary_sum + secondary_sum - mat[n // 2][n // 2] if n % 2 == 1 else primary_sum + secondary_sum


sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
result = sol.diagonalSum(mat)
print("Result:", result)