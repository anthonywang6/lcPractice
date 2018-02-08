import collections
class Solution:
    def ladderLength(self,beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #wordList.append(endWord)
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = collections.deque([(beginWord,1)])
        while queue:
            (word, length) = queue.popleft()

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] +c+word[i+1:] 
                    if next_word == endWord:
                        return length+1
                    if next_word in wordList:
                        queue.append((next_word,length+1))
                        wordList.remove(next_word)
        return 0

