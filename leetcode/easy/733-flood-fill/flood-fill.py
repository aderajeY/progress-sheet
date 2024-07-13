class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r,c = len(image), len(image[0])
        start_color = image[sr][sc] #Since we are replacing the value in the matrix, we MUST record our start color prior to any operation
        
        def paint_dfs(i,j): #here we set up our dfs function
            #for dfs function, I'd set up our boundaries first, so here comes boundaries for i and j
            if 0 <= i < r and 0 <= j < c and image[i][j] == start_color: #image[i][j]==start_color here because of the contraint of problem
                image[i][j] = color #paint new color
                return paint_dfs(i+1,j) and paint_dfs(i-1,j) and paint_dfs(i,j+1) and paint_dfs(i,j-1) #conduct our painting in adjacent square
                # [paint_dfs(i+x,j+y) for (x,y) in ((0,1),(1,0),(0,-1),(-1,0))] -----the alternative line of return, for your reference
            
            return image #else case, we simply return image without any operation, so image remains image
        
        if start_color != color: # we must exclude the case that start_color and color are the same, or it will turn out to be a infinite loop
            image = paint_dfs(sr,sc) #call the dfs function to start the operation
                
        return image # return image here because we change our color in image, without establishing any new matrix