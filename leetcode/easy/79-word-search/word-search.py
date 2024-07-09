class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        dir = [[-1,0],[0,1],[1,0],[0,-1]]
        def dfs(i,j,ind,ln,n,m):
            if ind == ln:
                return True
            if i<0 or j<0 or i>=n or j>=m or board[i][j] == 1 or board[i][j] != word[ind]:
                return False
            tmp = board[i][j]
            board[i][j] = 1
            ans = False
            for r,c in dir:
                new_r = i+r
                new_c = j+c
                ans = ans or dfs(new_r,new_c,ind+1,ln,n,m)
            board[i][j] = tmp
            return ans

        ans = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    ans = ans or dfs(i,j,0,len(word),n,m)
        return ans