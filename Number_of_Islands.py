class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        ret = 0
        length = len(grid)
        if length == 0:
            return 0
        width = len(grid[0])

        def DFS(x,y):
            grid[x][y] = '0'
            stepx = [0,1,-1,0]
            stepy = [1,0,0,-1]
            for k in range(4):
                x1 = x+stepx[k]
                y1 = y+stepy[k]
                if valid(x1,y1):
                    DFS(x1,y1)
        
        def valid(x,y):
            if x>=0 and x<length and y>=0 and y<width:
                if grid[x][y]=='1':
                    return True
            return False
        
        
        for i in range(length):
            for j in range(width):
                if valid(i,j):
                    DFS(i,j)
                    ret+=1
        return ret
