class TreeNode:
    def __init__(self, x):
        self.val =x
        self.left=None
        self.right=None

class Solution:
    def maxPathSum(self, root):
        return self.recMaxPathSum(root)[0]
    def recMaxPathSum(self,root):
        if not root:
            return (-1000,-1000)
        root_sum=root.val
        lbest, lsum = self.recMaxPathSum(root.left)
        rbest, rsum = self.recMaxPathSum(root.right)
        root_sum +=max(0,lsum)+max(0,rsum)
        best_sum =max(lbest,rbest,root_sum)
        return (best_sum, max(lsum,rsum)+root.val) 

