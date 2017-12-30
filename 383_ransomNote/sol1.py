import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_count= collections.defaultdict(int)
        m_count= collections.defaultdict(int)
        for i in range(ord('a'),ord('z')+1):
            c = chr(i)
            r_count[c]=ransomNote.count(c)
            m_count[c]=magazine.count(c)
        for c, v in r_count.items():
            if m_count[c]<v:
                return False
        return True

if __name__ == "__main__":
    ransomNote = 'aa'
    magazine = 'aab'

    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))

