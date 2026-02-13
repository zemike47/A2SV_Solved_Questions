
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 1️⃣ Length must be equal
        if len(word1) != len(word2):
            return False
        
        # 2️⃣ Count frequency of characters
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # 3️⃣ Same set of unique characters
        if set(count1.keys()) != set(count2.keys()):
            return False
        
        # 4️⃣ Same frequency distribution (order doesn't matter)
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        
        return True
