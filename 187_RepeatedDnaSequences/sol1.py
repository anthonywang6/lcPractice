class Solution:
    def findRepeatedDnaSequences(self,s):
        result=[]
        mem = collections.Counter()
        for itr in range(len(s)-10):
            dna = s[itr:itr+10]
            mem[dna]+=1 
            if mem[dna] ==2:
                result.append(dna)
        return result

