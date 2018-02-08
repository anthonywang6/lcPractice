import collections
class Solution:
    def minMutation(self, start, end, bank):
        bank = set(bank)
        queue = collections.deque([(start,0)])
        if end not in bank:
            return -1 

        while queue:
            (gene, length) = queue.popleft()
            for i in range(len(gene)):

                for dna in "ACGT":
                    mutation = gene[:i]+dna+gene[i+1:]
                    if mutation ==end:
                        return length +1
                    elif mutation in bank:
                        bank.remove(mutation)
                        queue.append((mutation,length+1))
        return -1 

