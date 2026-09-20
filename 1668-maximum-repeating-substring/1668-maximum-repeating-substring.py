class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        n = len(sequence)
        l = len(word)

        k = n // l

        count = 0
        repeated = ""
        
        for i in range(1,k+1):
            repeated += word

            if repeated in sequence:
                count += 1
        
        return count

        
