class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n ==0:
            return [0]

        g_codes=self.grayCode(n-1)
        rev_g_codes=[c+2**(n-1)for c in g_codes[::-1]]
        return g_codes+rev_g_codes



