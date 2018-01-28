class Solution:
    def numJewelsInStones(self, J, S):
        jtypes = [False]*(ord('z')-ord('A')+1)
        for j in J:
            jtypes[ord(j)-ord('A')]=True

        count =0
        for s in S:
            if jtypes[ord(s)-ord('A')]:
                count+=1

        return count

