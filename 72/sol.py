class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        l1,l2 = len(word1),len(word2)
        mem=[[0 for j in range(l2+1)] for i in range(l1+1)]
        for i in range(l1+1):
            mem[i][0]=i
        for j in range(l2+1):
            mem[0][j]=j

        for i in range(1,l1+1):
            for j in range(1,l2+1):
                mem[i][j]=min(mem[i-1][j],mem[i][j-1]) +1
                mem[i][j]= min(mem[i][j],mem[i-1][j-1]+ (0 if word1[i-1]==word2[j-1]else 1))
        print(mem)
        return mem [-1][-1]



