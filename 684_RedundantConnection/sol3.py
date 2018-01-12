class DSU:
    def __init__(self):
        """
        1st speed up union by rank
        2nd speed up path compression during find
        """
        self.par = [i for i in range(1001)] # each one has itself as parent
        self.rnk = [0]*1001 # record rank for speeding up

    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return False
        elif self.rnk[xp]< self.rnk[yp]:
            self.par[xp]=yp
        elif self.rnk[xp]>self.rnk[yp]:
            self.par[yp]=xp
        else:
            self.par[yp]=xp
            self.rnk[xp]+=1
        return True

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges List[List[int]]
        :rtype List[int]
        """
        dsu = DSU()
        for s,t in edges:
            if not dsu.union(s,t):
                return [s,t]
