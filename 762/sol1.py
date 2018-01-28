class Solution:
    def countPrimeSetBits(self, L, R):
        primes=set([2,3,5,7,11,13,17,19,23])
        res =0

        for n in range(L,R+1):
            bits =bin(n).count("1")
            if bits in primes:
                res +=1
        return res




