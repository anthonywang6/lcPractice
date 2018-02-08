class Solution:
    def slidingPuzzle(self, board):
        state = "".join([str(n) for row in board for n in row])
        ans = "123450"
        if state ==ans:
            return 0
        mem = set()
        mem.add(state)
        queue = [(state,0)]
        while queue:
            state, step= queue.pop(0)
            #print("state:"+state+"   {} steps".format(step))
            zp = state.find('0')

            if zp-1>=0 and zp !=3:
                nstate= [s for s in state]
                nstate[zp],nstate[zp-1]=nstate[zp-1],nstate[zp]
                nstate= "".join(nstate)
                #print("   left: "+nstate)
                if nstate ==ans:
                    return step+1
                if nstate not in mem:
                    mem.add(nstate)
                    queue.append((nstate,step+1))
            if zp-3>=0:
                nstate= [s for s in state]
                nstate[zp],nstate[zp-3]=nstate[zp-3],nstate[zp]
                nstate= "".join(nstate)
                #print("   up: "+nstate)
                if nstate ==ans:
                    return step+1
                if nstate not in mem:
                    mem.add(nstate)
                    queue.append((nstate,step+1))
            if zp+1<6 and zp!=2:
                nstate= [s for s in state]
                nstate[zp],nstate[zp+1]=nstate[zp+1],nstate[zp]
                nstate= "".join(nstate)
                #print("   right: "+nstate)
                if nstate ==ans:
                    return step+1
                if nstate not in mem:
                    mem.add(nstate)
                    queue.append((nstate,step+1))
            if zp+3<6:
                nstate= [s for s in state]
                nstate[zp],nstate[zp+3]=nstate[zp+3],nstate[zp]
                nstate= "".join(nstate)
                #print("   down: "+nstate)
                if nstate ==ans:
                    return step+1
                if nstate not in mem:
                    mem.add(nstate)
                    queue.append((nstate,step+1))
        return -1


if __name__ == "__main__":
    board =[[3,2,4],[1,5,0]]
    sol = Solution()
    result = sol.slidingPuzzle(board)
    print(result)
