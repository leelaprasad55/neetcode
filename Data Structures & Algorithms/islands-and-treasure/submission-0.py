from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])
        inf=2147483647
        q=deque()
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            ki,kj=q.popleft()
            for vx,vy in d:
                mx,my=vx+ki,vy+kj
                if 0<=mx<m and 0<=my<n and grid[mx][my]==inf:
                    grid[mx][my]=grid[ki][kj]+1
                    q.append((mx,my))