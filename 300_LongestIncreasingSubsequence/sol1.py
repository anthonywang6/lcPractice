class Solution:
    def lengthOfLIS(self, nums)
    """
    :type nums: List[int]
    :rtype int
    """
    if not nums:
        return 0
    nsize =len(nums) 
    mem = [0]*nsize
    for i in range(nsize)[::-1]:
        j=1
        best=1
        while i+j<nsize:
            if nums[i]< nums[i+j]:
                best = max(best, mem[i+j]+1)
            j+=1
        mem[i]=best
    return max(mem)
        

