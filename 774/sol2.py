import math
class Solution:
    def minmaxGasDist(self, st, K):
        left,right = 1e-6, st[-1] - st[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            print("l,r,m == {},{},{}".format(left, right, mid))
            count = 0
            for a, b in zip(st, st[1:]):
                count += max(0, math.ceil((b - a) / mid) - 1)
            print("count:{}".format(count)) 
            if count > K:
                left = mid
            else:
                right = mid
        return right




if __name__ == "__main__":
    st= [10,19,25,27,56,63,70,87,96,97]
    K=3
    sol = Solution()
    res= sol.minmaxGasDist(st,K)
