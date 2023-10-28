# Robot Bounded In Circle

'''On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:
"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.'''

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        direction = 'N' 
        clockwise_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

        for instruction in instructions:
            if instruction == 'G':
                dx, dy = moves[direction]
                x, y = x + dx, y + dy
            elif instruction == 'L':
                direction = clockwise_turn[direction]
            elif instruction == 'R':
                direction = clockwise_turn[clockwise_turn[clockwise_turn[direction]]]

        return (x, y) == (0, 0) or direction != 'N'

sol = Solution()
instructions = "GGLLGG"
result = sol.isRobotBounded(instructions)
print("Result:", result)