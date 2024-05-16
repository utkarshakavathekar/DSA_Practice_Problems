class Solution:
    def solveNQueens(self, n):
        boardRow = "."*n
        board = [boardRow]*n
        ans  = list()
        # hash map to check if any Quene is present in current row, hashindex is row
        leftRow = [0]*n
        # hash map to check if any Quene is present in current row,col where hashindex is(n-1)+(col-row)
        upperDiagonal = [0]*((2*n)-1)
        # hash map to check if any Quene is present in current row,col where hashindex is(row+col)
        lowerDiagonal = [0]*((2*n)-1)
        self.findQueenIndex(0,board,ans,leftRow,upperDiagonal,lowerDiagonal,n)
        return ans

    def findQueenIndex(self,col,board,ans,leftRow,upperDiagonal,lowerDiagonal,n):
        if col==n:
            ans.append(board.copy())
            return
        
        for row in range(0,n):
            if leftRow[row]==0 and upperDiagonal[(n-1)+(col-row)]==0 and lowerDiagonal[row+col]==0:
                board[row] = board[row][:col] + 'Q' + board[row][col+1:] #as string assigmnet can not be done in python
                
                leftRow[row] = 1
                upperDiagonal[(n-1)+(col-row)]=1
                lowerDiagonal[row+col]=1

                self.findQueenIndex(col+1,board,ans,leftRow,upperDiagonal,lowerDiagonal,n)
                
                leftRow[row] = 0
                upperDiagonal[(n-1)+(col-row)]=0
                lowerDiagonal[row+col]=0
                
                board[row] = board[row][:col] + '.' + board[row][col+1:]
