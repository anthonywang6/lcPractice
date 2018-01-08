class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left =None
        self.right=None
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isvBST(root)[0]

    def isvBST(self,root):
        m =M= root.val
        left= root.left
        right=root.right

        if left:
            (lv,lm,lM)=self.isvBST(root.left)
            if not lv or root.val<=lM:
                return (False,m,M)
            m=lm
        if right:
            (rv,rm,rM)=self.isvBST(root.right)
            if not rv or root.val>=rm:
                return (False,m,M)
            M=rM

        return (True, m, M)



