class Solution(object):
    def numTrees(self, n):
        if not n:
            return 0
        self.mem=[ -1 for i in range(n+1) ]
        self.mem[0]=1
        self.mem[1]=1
        self.mem[2]=2
        return self.recNumTrees(n)

    def recNumTrees(self,n):
        if self.mem[n]>=0:
            return self.mem[n]

        cul=0
        for i in range(1, n+1):
            left = self.recNumTrees(i-1)
            right = self.recNumTrees(n-i)
            cul+=left*right
        self.mem[n]=cul
        return cul


        
