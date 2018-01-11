class Solution:
    def sortColors(self, nums):
        #bubble sort
        for i, n in enumerate(nums):
            j=i
            while j>0 and nums[j]<nums[j-1]:
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j-=1

