# Check If It Is a Straight Line

''' You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate 
of a point. Check if these points make a straight line in the XY plane.'''

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 3:
            return True  
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x1) * (y2 - y1) != (x2 - x1) * (y - y1):
                return False
        return True

sol = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
result = sol.checkStraightLine(coordinates)
print("Result:", result)
