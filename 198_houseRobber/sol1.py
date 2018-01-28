class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums)==1:
            return nums[0]
        nsize= len(nums)
        mem = [0]*nsize
        mem[0]=nums[0]
        mem[1]=max(nums[0],nums[1])

        for i in range(2,nsize):
            mem[i] = max(nums[i]+mem[i-2],mem[i-1])

        return  max(mem[-1],mem[-2])
