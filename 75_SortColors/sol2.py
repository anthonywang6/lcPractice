class Solution:
    def sortColors(self, nums):
        count=[0]*3
        for  n in nums:
            count[n]+=1
        i =0
        for x, c in enumerate(count):
            for j in range(c):
                nums[i+j]=x
            i+=c+1

