class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        hash_map = defaultdict(list)

        for st in strs:
            count = [0] * 26

            for c in st:
                i = ord(c) - ord('a')
                count[i] += 1

            
            hash_map[tuple(count)].append(st)
            
        return list(hash_map.values())





            




        



            


        
