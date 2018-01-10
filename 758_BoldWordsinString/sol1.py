import collections

class Node:
    def __init__(self,c,l,end):
        self.chr=c
        self.length=l
        self.end=end
        self.nexts={}

class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S:str
        :rtype: str
        """
        root = self.createSearchTree(words)
        flags =[False]*len(S)

        cursors=[]
        for s_itr,s in enumerate(S):
            n_cursors=[]
            while cursors:
                csr = cursors.pop()
                if csr.end:
                    for r in range(csr.length):
                        flags[s_itr-r-1]=True
                if s in csr.nexts:
                    print('next:{}'.format(s))
                    n_cursors.append(csr.nexts[s])
            cursors=n_cursors

            if s in root.nexts:
                print('add: {}'.format(s))
                cursors.append(root.nexts[s])

        while cursors:
            csr = cursors.pop()
            if csr.end:
                for r in range(csr.length):
                    flags[s_itr-r]=True


        # generate the string
        result =[]
        pre=False
        for itr,f in enumerate(flags):
            if f==pre:
                result.append(S[itr])
            elif f and not pre:
                result+=['<b>',S[itr]]
            elif not f and pre:
                result+=['</b>',S[itr]]
            pre =f 
        if flags[-1]:
            result.append('</b>')
        return ''.join(result)




    def createSearchTree(self, words):
        root = Node("",0,False)
        for word in words:
            cur =root
            for c in word:
                if c not in cur.nexts:
                    cur.nexts[c]=Node(c, cur.length+1, False)
                cur = cur.nexts[c]
            cur.end=True
        return root
