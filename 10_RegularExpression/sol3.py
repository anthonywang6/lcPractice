class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.mtx=[[-1 for j in range(len(p)+1)]for i in range(len(s)+1)]
        self.mtx[0][0]=1
        return self.is_Match(s,p,0,0)

    def is_Match(self,s, p, i, j):
        if not self.mtx[i][j]:
            return False

        while i<=len(s) and j<len(p):
            if j+1<len(p) and p[j+1]=='*':
                if i<len(s) and self.match(s[i],p[j]):
                    res=self.is_Match(s,p,i,j+2) or self.is_Match(s,p,i+1,j+2) or self.is_Match(s,p,i+1,j)
                    self.mtx[i][j]=res
                    return res

                else:
                    res =self.is_Match(s,p,i,j+2)
                    self.mtx[i][j]=res
                    return res


            elif i<len(s) and self.match(s[i],p[j]):
                i+=1
                j+=1
            else:
                res= False
                self.mtx[i][j]=res
                return res
        res=True if i==len(s) and j==len(p) else False
        self.mtx[i][j]=res
        return res

    def match(self,sc,pc):
        return sc==pc or pc=='.'


if __name__ == "__main__":
    s = "aa"
    p = "a*"
    sol = Solution()
    print(sol.isMatch(s,p))
