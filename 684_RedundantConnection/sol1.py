class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges List[List[int]]
        :rtype List[int]
        """
        graph =collections.defaultdict(set)

        def dfs(source,target):
            if source == target: return True
            if source not in seen:
                seen.add(source)
                return any( dfs(nei,target) for nei in graph[source])

            return False

        for s,t in edges:
            seen=set()
            if dfs(source,target):
                return [s,t]
            graph[s].add(t)
            graph[t].add(s)
            
