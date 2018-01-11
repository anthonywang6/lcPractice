class Solution:
    def pourWater(self,heights,V,K):
        while V>0:
            self.checkFall(heights,K) 
            V-=1
        return heights

    def checkFall(self,heights,K):
        cur=i= K
        h=heights[cur]
        while i>=0 and heights[i]<=h:
            if heights[i]<h:
                cur =i
                h=heights[i]
            i-=1
        if cur !=K:
            heights[cur]+=1
            return 
        i=K
        while i<len(heights) and heights[i]<=h:
            if heights[i]<h:
                cur=i
                h=heights[i]
            i+=1
        heights[cur]+=1
