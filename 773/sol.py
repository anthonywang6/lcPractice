class Solution:
    def slidingPuzzle(self, board):
        state = "".join([str(n) for row in board for n in row])
        ans = "123450"
        if state ==ans:
            return 0
        mem = {state:1}
        queue = [(state,0)]
        while queue:
            state, step= queue.pop(0)
            #print("state:"+state)
            zp = state.find('0')
            if zp-1>=0:
                next = state[:zp-1]+'0'+state[zp-1]+state[zp+1:]
                #print("left: "+next)
                if next ==ans:
                    return step+1
                if next not in mem:
                    mem[next]=1
                    queue.append((next,step+1))
            if zp-3>=0:
                next = state[:zp-3]+'0'+state[zp-2:zp]+state[zp-3]+state[zp+1:]
                #print("up: "+next)
                if next ==ans:
                    return step+1
                if next not in mem:
                    mem[next]=1
                    queue.append((next,step+1))
            zp = state.find('0')
            if zp+1<6:
                next = state[:zp]+state[zp+1]+'0'+state[zp+2:]
                #print("right:"+next)
                if next ==ans:
                    return step+1
                if next not in mem:
                    mem[next]=1
                    queue.append((next,step+1))
            if zp+3<6:
                next = state[:zp]+state[zp+3]+state[zp+1:zp+3]+'0'+state[zp+4:]
                #print("down:"+next)
                if next ==ans:
                    return step+1
                if next not in mem:
                    mem[next]=1
                    queue.append((next,step+1))
        return -1
