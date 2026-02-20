class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        name_height_map = {}

        for i in range(len(names)):
            name_height_map[heights[i]] = names[i]
        
        name_height_map = dict(sorted(name_height_map.items(),reverse=True))
        #print(name_height_map)

        ans = [ name for name in name_height_map.values()]
        return ans