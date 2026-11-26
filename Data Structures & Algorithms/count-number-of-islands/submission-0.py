class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        c=0

        def bfs(i,j):
            if i>=m or i<0 or j>=n or j<0:
                return 
            if grid[i][j]=='0':
                return 
            grid[i][j]='0'
            bfs(i,j-1)
            bfs(i,j+1)
            bfs(i-1,j)
            bfs(i+1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    c+=1
                    bfs(i,j)
        return c