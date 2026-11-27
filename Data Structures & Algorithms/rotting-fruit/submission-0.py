
class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        grid = g
        m, n = len(grid), len(grid[0])
        c = 0
        r = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    c += 1

        while q and c > 0:
            r += 1
            l = len(q)

            for _ in range(l):
                i, j = q.popleft()

                if i < 0 or j < 0 or i >= m or j >= n:
                    continue

                if grid[i][j] == 0:
                    continue

                for x, y in [(i,j-1), (i,j+1), (i-1,j), (i+1,j)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        q.append((x,y))
                        c -= 1
                        grid[x][y] = 2

        return -1 if c > 0 else r
