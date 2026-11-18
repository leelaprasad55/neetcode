class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m,n=len(board),len(board[0])
        b1=board
        b2=[['' for _ in range(n)] for _ in range(m)]
        d={}
        for i in range(m):
            for j in range(n):
                d[str(i//3)+str(j//3)]=[]
        for i in range(m):
            for j in range(n):
                d[str(i//3)+str(j//3)].append(board[i][j])
        for i in range(m):
            for j in range(n):
                b2[i][j]=b1[j][i]
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    c1=b1[i].count(board[i][j])
                    c2=b2[j].count(board[i][j])
                    c3=d[str(i//3)+str(j//3)].count(board[i][j])
                    if c1 > 1 or c2 > 1 or c3 > 1:
                        return False
        return True
