class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList_set = set(wordList)

        if endWord not in wordList_set:
            return 0

        distance = 1

        queue = deque([(beginWord,distance)])

        while queue:
            word , distance= queue.popleft()

            if word == endWord:
                return distance

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:i] + c + word[i+1:]

                    if new_word in wordList_set:
                        wordList_set.remove(new_word)
                        queue.append((new_word,distance+1))

        return 0
        
                        
