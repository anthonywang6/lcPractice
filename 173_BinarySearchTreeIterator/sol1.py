class BSTIterator(object):
    def __init__(self,root):
        self.stack=[]
        self.pushLeft(root)
        pass
    def hasNext(self):
        return self.stack 
    def next(self):
        pop = self.stack.pop()
        if pop.right:
            self.pushLeft(pop.right)
        return pop.val

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

