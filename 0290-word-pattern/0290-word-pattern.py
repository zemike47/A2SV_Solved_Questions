class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        slist = s.split()

        hash_map1 = {}
        hash_map2 = {}

        for i in range(len(pattern)):
            if pattern[i] in hash_map1:
                if hash_map1[pattern[i]] != slist[i]:
                    return False
            else:
                hash_map1[pattern[i]] = slist[i]

            
            if slist[i] in hash_map2:
                if hash_map2[slist[i]] != pattern[i]:
                    return False
            else:
                hash_map2[slist[i]] = pattern[i]

        return True
