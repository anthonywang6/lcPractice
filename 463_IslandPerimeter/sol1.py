class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Question: is there better way to find the first land
        # DFS
        if not grid:
            return 0
        visit = collections.Counter()
        l = len(grid)
        w = len(grid[0])
        stack =[]
        pmeter=0
        i=j=0
        # seek for land
        while not grid[i][j]:
            if j+1<w:
                j = j+1
            else:
                j=0
                i=i+1

        # BFS travel on the land
        stack.append((i,j))
        visit[(i,j)]+=1
        while stack:
            (i,j) = stack.pop(0)
            count = 0
            if i-1>=0 and grid[i-1][j] and not visit[(i-1,j)]:
                stack.append((i-1,j))
                visit[(i-1,j)]+=1

            if j-1>=0 and grid[i][j-1] and not visit[(i,j-1)]:
                stack.append((i,j-1))
                visit[(i,j-1)]+=1

            if j+1<w and grid[i][j+1] and not visit[(i,j+1)]:
                stack.append((i,j+1))
                visit[(i,j+1)]+=1

            if i+1<l and grid[i+1][j] and not visit[(i+1,j)]:
                stack.append((i+1,j))
                visit[(i+1,j)]+=1

            pmeter += 1 if i==0 or not grid[i-1][j] else 0
            pmeter += 1 if j==0 or not grid[i][j-1] else 0
            pmeter += 1 if i==l-1 or not grid[i+1][j] else 0
            pmeter += 1 if j==w-1 or not grid[i][j+1] else 0

            visit[(i,j)]+=1
            print("{}, p={}".format((i,j),pmeter))
        return pmeter
