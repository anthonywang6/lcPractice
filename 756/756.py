import collections
class Solution:
    def pyramidTransition(self,bottom, allowed):
        self.error={}
        self.map=collections.defaultdict(list)
        for a in allowed:
            self.map[a,[0],a[1]].append(a[2])

        return self.rec_method(bottom,allowed)

    def rec_method(self, bottom,allowed):
        if len(bottom) ==1:
            return True
        if bottom in self.error:
            return False
        candids =[]
        for i,b in enumerate(bottom[1:]):
            if (bottom[i-1],b) not in self.map:
                self.error[bottom]=1
                return False
            else:
                candids.append(self.map[bottom[i-1],b])
        nlevels=[]
        nlevels=self.getNext(candids,0,nlevels)

    def getNext(self,candids, i, temp, nlevel):
        if i==len(candids):
            return
        for c in candids[i]: 
            temp.append(c)
            getNext(self,candids,i+1,temp,nlevel)

