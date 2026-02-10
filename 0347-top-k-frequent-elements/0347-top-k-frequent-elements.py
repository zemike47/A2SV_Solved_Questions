class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        arr = c.most_common(k)
        ans = []



        for i in range(len(arr)):
            ans.append(arr[i][0])

        return ans

