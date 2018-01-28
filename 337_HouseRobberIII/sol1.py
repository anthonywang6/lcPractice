class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def rob(root):
            lrob=lskp=0
            rrob=rskp=0
            if root.left:
                (lrob,lskp) = rob(root.left)
            if root.right:
                (rrob,rskp) = rob(root.right)

            rrob = root.val + lskp +rskp
            rskp = max(rrob,rskp)+max(lrob,lskp)
            return (rrob,rskp)

        return max(rob(root))
