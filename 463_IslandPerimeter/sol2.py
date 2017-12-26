class Solution(object):
    def islandPerimeter(self,grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0
        p=0
        l = len(grid)
        w = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    p+= 1 if (i==0 or not grid[i-1][j]) else 0
                    p+= 1 if (i==l-1 or not grid[i+1][j]) else 0
                    p+= 1 if (j==0 or not grid[i][j-1]) else 0
                    p+= 1 if (j==w-1 or not grid[i][j+1]) else 0
        return p
