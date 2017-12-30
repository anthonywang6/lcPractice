class Solution:
    def connect(self,root):
        if not root:
            return root
        head =root
        while head.left:
            cur=head
            cur.left.next=cur.right
            while cur.next:
                cur.right.next= cur.next.left 
                cur.next.left.next=cur.next.right
                cur=cur.next
            head=head.left
