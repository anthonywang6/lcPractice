class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result= [[]]
        for n in nums:
            for r in range(len(result)):
                result.append(result[r]+[n])
        return result


if __name__ =="__main__":
    nums = [1,2,3]
    sol = Solution()
    result = sol.subsets(nums)
    print(result)
