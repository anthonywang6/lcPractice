class Solution(object):
    def groupAnagrams(self, strs):
        result = collections.defaultdict(list)
        for s in strs:
            key=[0 for i in range(26)]
            _set = set(s)
            for ss in _set:
                key[ord(ss)-ord("a")]=s.count(ss)

            result[tuple(key)].append(s)
        return [ v for k,v in result.items() ]
