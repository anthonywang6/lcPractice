class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        big = small = M = nums[0]

        for n in nums[1:]:
            big ,small= max(n,n*big,n*small), min(n,n*big,n*small)
            M = max(M,big)

        return M

