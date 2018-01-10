class TreeNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            p = preorder.pop(0)
            iidx=inorder.index(p)
            root =TreeNode(p)
            root.left =self.buildTree(preorder,inorder[:iidx])
            root.right=self.buildTree(preorder,inorder[iidx+1:])
            return root
