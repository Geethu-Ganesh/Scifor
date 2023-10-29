# Spiral Matrix

''' Given an m x n matrix, return all elements of the matrix in spiral order.'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            result += matrix[0]
            matrix = list(zip(*matrix[1:]))[::-1]
        return result

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = sol.spiralOrder(matrix)
print("Result:", result)
