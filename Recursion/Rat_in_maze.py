#User function Template for python3

class Solution:
    def findPath(self, matrix, n):
        # code here
        
        visited = [[0 for _ in range(n)] for _ in range(n)]
        i,j=0,0
        ans = []
        curr_path = ""
        if matrix[i][j]==1:
            self.getPossiblePaths(i, j, matrix, curr_path, visited, ans, n)
        return ans
     
    def getPossiblePaths(self, i, j, matrix, curr_path, visited, ans, n):
        
        if i==n-1 and j==n-1:
            ans.append(curr_path)
            return
    
        if i+1<n and visited[i+1][j]==0 and matrix[i+1][j]==1:
            visited[i][j]=1
            self.getPossiblePaths(i+1, j, matrix, curr_path+'D', visited, ans, n)
            visited[i][j]=0
            
        if j-1>=0 and visited[i][j-1]==0 and matrix[i][j-1]==1:
            visited[i][j]=1
            self.getPossiblePaths(i, j-1, matrix, curr_path+'L', visited, ans, n)
            visited[i][j]=0
            
        if j+1<n and visited[i][j+1]==0 and matrix[i][j+1]==1:
            visited[i][j]=1
            self.getPossiblePaths(i, j+1, matrix, curr_path+'R', visited, ans, n)
            visited[i][j]=0
            
        if i-1>=0 and visited[i-1][j]==0 and matrix[i-1][j]==1:
            visited[i][j]=1
            self.getPossiblePaths(i-1, j, matrix, curr_path+'U', visited, ans, n)
            visited[i][j]=0
            

###########################################################################################################################

#################    This 4 recursion calls can be reduced to one by creating hashset     #################################


class Solution:
    def findPath(self, matrix, n):
        # code here
        
        visited = [[0 for _ in range(n)] for _ in range(n)]
        i,j=0,0
        ans = []
        curr_path = ""
        rowMoves = [1, 0, 0, -1]
        colMoves = [0, -1, 1, 0]
        moves = 'DLRU'
        if matrix[i][j]==1:
            self.getPossiblePaths(i, j, matrix, curr_path, visited, ans, n, rowMoves, colMoves, moves)
        return ans
     
    def getPossiblePaths(self, row, col, matrix, curr_path, visited, ans, n, rowMoves, colMoves, moves):
        
        if row==n-1 and col==n-1:
            ans.append(curr_path)
            return

        for i in range(0,4):
            newRow = row+rowMoves[i]
            newCol = col+colMoves[i]

            ch = moves[i]
    
            if newRow<n and newCol<n and newRow>=0 and newCol >=0 and visited[newRow][newCol]==0 and matrix[newRow][newCol]==1:
                visited[row][col]=1
                self.getPossiblePaths(newRow, newCol, matrix, curr_path+ch, visited, ans, n, rowMoves, colMoves, moves)
                visited[row][col]=0
