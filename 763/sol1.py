class Solution:
    def partitionLabels(self, S):
        res=[]
        seen=set()
        intervals =[]
        for i, s in enumerate(S):
            if s not in seen:
                intervals.append((i,S.rfind(s)))
                seen.add(s)
        intervals.sort()
        pre=intervals[0]
        for itvl in intervals[1:]:
            if itvl[0]<=pre[1]:
                pre=(pre[0],max(itvl[1],pre[1]))
            else:
                res.append(pre[1]-pre[0])
                pre=itvl
        return res

             

