class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        hash_table = {}

        for i , char in enumerate(order):
            hash_table[char] = i

        for i in range(len(words)-1):
            word1 = words[i]

            for j in range(i+1,i+2):
                word2 = words[j]
                min_len = min(len(word1),len(word2))
                w1 = 0
                w2 = 0

                while w1 < min_len and w2 < min_len:

                    if hash_table[word1[w1]] == hash_table[word2[w2]]:
                        w1  += 1
                        w2 += 1
                    
                    elif hash_table[word1[w1]] > hash_table[word2[w2]]:
                        return False
                    else:
                        break
           

                if  w1 == min_len and len(word1) > len(word2):
                    return False
            
        return True 






