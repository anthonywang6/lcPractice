class Solution:
    def addBinary(self,a,b):
        # best solution
        # return bin(eval("0b"+a)+eval("0b"+b))[2:] 

        # solution2 
        return bin(int(a,2)+int(b,2))[2:] 
        
        pass

