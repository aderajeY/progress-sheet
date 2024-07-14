class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Method1: DFS.
        def dfs(x, y):
            if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0])-1 or board[x][y] != 'O':
                return
            board[x][y] = 'A'
            dfs(x+1, y) # Down
            dfs(x-1, y) # Up
            dfs(x, y-1) # Left
            dfs(x, y+1) # Right
            return

        m, n = len(board), len(board[0]) # m = row, n = col
        for i in range(m):
            dfs(i, 0) # First col
            dfs(i, n-1) # Last col
        for j in range(n):
            dfs(0, j) # First row
            dfs(m-1, j) # Last row
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        return