class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S:str
        :rtype: str
        """
        res =[]
        count=i=0
        for j, s in enumerate(S):
            count += 1 if s=='1' else -1
            if count==0:
                res.append('1'+self.makeLargestSpecial(S[i+1:j])+'0')
                i=j+1
        return ''.join(sorted(res)[::-1])

