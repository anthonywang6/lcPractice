class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur= root
        maxv = max(p.val,q.val)
        minv = min(p.val,q.val)
        while cur.val<minv or  cur.val>maxv :
            if cur.val > minv:
                cur=cur.left 
            elif cur.val < maxv:
                cur=cur.right 
        return cur
