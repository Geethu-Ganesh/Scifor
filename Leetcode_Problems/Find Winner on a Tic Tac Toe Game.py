# Find Winner on a Tic Tac Toe Game

''' Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played 
on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a 
draw return "Draw". If there are still movements to play return "Pending".
You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially 
empty, and A will play first.'''

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        is_A_turn = True
        def check_winner(player):
            for i in range(3):
                if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
                    return True
            if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
                return True
            return False

        for move in moves:
            row, col = move
            if is_A_turn:
                grid[row][col] = 'X'
                if check_winner('X'):
                    return "A"
            else:
                grid[row][col] = 'O'
                if check_winner('O'):
                    return "B"
            is_A_turn = not is_A_turn

        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"
        

sol = Solution()
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
result = sol.tictactoe(moves)
print("Result:", result)
        