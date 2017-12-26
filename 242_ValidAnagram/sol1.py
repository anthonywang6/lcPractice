class Solution(object):
    def isAnagram(self,s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = collections.Counter()
        for ss in s:
            count[ss]+=1
        for tt in t:
            count[tt]-=1

        for k, v in count.items():
            if v:
                return False
        return True
