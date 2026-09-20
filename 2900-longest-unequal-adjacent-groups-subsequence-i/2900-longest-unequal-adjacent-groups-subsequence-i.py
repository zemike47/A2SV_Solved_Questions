class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        last_group = groups[0]
        result = [words[0]]

        for i in range(1,len(groups)):
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]

        return result
