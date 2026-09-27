class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        n = len(nums)


        freq = Counter(nums)

        count = [[] for _ in range(n+1)]

        for num , freq in freq.items():
            count[freq].append(num)

        ans = []
        for i in range(n,-1,-1):
            for num in count[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans

         
