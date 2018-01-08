class Interval:
    def __init__(self,s=0,e=0):
        self.start =s
        self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        schedule = [interval for em in schedule for interval in em]
        avails = sorted(schedule, key=lambda interval: interval.start)

        stack = [avails[0]]
        res =[]
        for cur in avails[1:]:
            top = stack.pop()
            if top.end=>cur.start:
                stack.append(Interval(top.start,max(top.end,cur.end)))
            else:
                res.append(Interval(top.end,cur.start))
                stack.append(cur)
        return res 


