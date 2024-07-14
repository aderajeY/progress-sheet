class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()

        
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        #queue dist, source, end
        queue.append((1,0,0))
        distance = set()

        distance.add((0,0))
        if grid[0][0] !=0 or grid[n-1][m-1] != 0:
            return -1
        while queue:
            dist, cx, cy = queue.popleft()
            if cx == n-1 and cy == m-1:
                return dist

            for dx, dy in directions:
                nx, ny = cx+dx, cy+dy

                if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 0 and (nx,ny) not in distance:
                    distance.add((nx,ny))
                    queue.append((dist+1, nx,ny))
                        
                   
        return -1

                    


