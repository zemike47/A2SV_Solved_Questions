class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine) 

        for key,value in r_counter.items():
            if key not in m_counter:
                return False
            elif value > m_counter[key]:
                return False
        else:
            return True



        