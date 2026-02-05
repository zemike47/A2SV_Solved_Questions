class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        output = 0
        
        chars_counter = Counter(chars)
        
        for word in words:
            word_counter = Counter(word)

            for c in word:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                output = output + len(word)
                
                

        
        return output


            
            