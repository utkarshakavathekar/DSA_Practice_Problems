class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):

                if board[i][j]=='.':
                    for c in range(1,10):
                        if self.isValid(board,i,j,c):
                            board[i][j] = str(c)

                            if self.solve(board)==True:
                                return True
                            else:
                                board[i][j] = '.'

                    return False
        return True
    
    def isValid(self,board,row,col,c):
        for i in range(0,len(board)):
            if board[i][col]==str(c):
                return False
            if board[row][i]==str(c):
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==str(c):
                return False
        return True
