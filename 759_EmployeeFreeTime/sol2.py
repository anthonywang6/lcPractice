from heapq import *
from functools import reduce
class Interval:
    def __init__(self, s=0, e=0):
        self.start =s
        self.end =e

class Solution:
    def employeeFreeTime(self, schedule):
        # ***flat the list***
        # schedule = [interval for em in schedule for interval in em]
        # reduce practice
        schedules = reduce(lambda x,y: x+y, schedule)

        # ***heap sort***
        intvls=[]
        count = collections.defaultdict(int)
        for intvl in schedules:
            count[intvl.start]+=1
            heappush(intvls,(intvl.start,count[intvl.start], intvl))

        cur = heappop(intvls)[2]
        result=[]
        while intvls:
            top = heappop(intvls)[2]
            if cur.end >= top.start:
                cur.end=max(top.end, cur.end)
            else:
                result.append(Interval(cur.end, top.start))
                cur= top
        return result



