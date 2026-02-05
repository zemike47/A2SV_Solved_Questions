class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_string_map = {}
        ans = []
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])

                common_string_map[list1[i]] = i + j
        

        least_common_idx = min(common_string_map.values())

        for key,value in common_string_map.items():
            if value <= least_common_idx:
                ans.append(key)

    

        return ans



        