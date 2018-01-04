class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_Match(s,p,0,0)

    def is_Match(self,s, p, i, j):
        print('{},{}'.format(i,j))
        while i<=len(s) and j<len(p):
            if j+1<len(p) and p[j+1]=='*':
                if i<len(s) and self.match(s[i],p[j]):
                    return self.is_Match(s,p,i,j+2) or self.is_Match(s,p,i+1,j+2) or self.is_Match(s,p,i+1,j)
                else:
                    return self.is_Match(s,p,i,j+2)

            elif i<len(s) and self.match(s[i],p[j]):
                i+=1
                j+=1
            else:
                return False
        return True if i==len(s) and j==len(p) else False

    def match(self,sc,pc):
        return sc==pc or pc=='.'


if __name__ == "__main__":
    s = "aa"
    p = "a*"
    sol = Solution()
    print(sol.isMatch(s,p))
