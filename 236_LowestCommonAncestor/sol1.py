class Solution(object):
    def lowestCommonAncestor(self, root, p ,q):
        curpath=[]
        paths=[]
        self.findNodes(root, [node.val for node in [p,q]], curpath, paths)

        minlen = min(len(paths[0]), len(paths[1]))
        i = 0
        while i+1<minlen and paths[0][i+1] == paths[1][i+1]:
            i+=1
        return paths[0][i]

    def findNodes(self, node, labels, curpath, paths):
        if not node :
            return
        curpath.append(node)
        if node.val in labels:
            paths.append([node for node in curpath])
        self.findNodes(node.left, labels, curpath, paths)
        self.findNodes(node.right, labels, curpath, paths)
        curpath.pop()

