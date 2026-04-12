from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if endWord not in word_set:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, length = queue.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for c in alphabet:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        queue.append((new_word, length + 1))
                        word_set.remove(new_word)

        return 0
