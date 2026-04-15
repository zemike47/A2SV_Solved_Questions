class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []

        cnt = collections.Counter(nums)

        cnt = sorted(cnt.items(),key = lambda x:x[1],reverse=True)
        ans.append(cnt[0][0])

        set_nums = set(nums)
        # print(len(nums))

        for i in range(1,len(nums)+1):
            if i not in set_nums:
                # print(i)
                ans.append(i)
                break
        
        return ans




