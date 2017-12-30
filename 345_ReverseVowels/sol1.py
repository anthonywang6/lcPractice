class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        result=['']*len(s)
        l=0
        r=len(s)-1
        while l<r:
            while l<r and (s[l].lower() not in vowels):
                result[l]=s[l]
                l+=1
            while l<r and (s[r].lower() not in vowels):
                result[r]=s[r]
                r-=1
            result[l]=s[r]
            result[r]=s[l]
            l+=1
            r-=1
        return "".join(result)


if __name__ == "__main__":
    s = 'hello'
    sol = Solution()
    print(sol.reverseVowels(s))
