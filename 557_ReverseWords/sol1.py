class Solution(object):
    def reverseWords(self, s):
        """
        :type s :str
        :rtype: str
        """
        ss=" ".join(s[::-1].split()[::-1])
        return ss


