class Solution:
    def firstUniqChar(self,s):
        count =collections.Counter()
        for ss in s:
            count[ss]+=1
        for itr, ss enumerate(s):
            if count[ss]==1:
                return itr
        return -1
