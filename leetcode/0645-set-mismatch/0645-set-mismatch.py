class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []

        # cnt = collections.Counter(nums)

        # cnt = sorted(cnt.items(),key = lambda x:x[1],reverse=True)
        # ans.append(cnt[0][0])

        set_nums = set(nums)
        # # print(len(nums))
        cnt = [0] * len(nums) 
        miss = 0
        duplicat = 0


        for i in range(1,len(nums)+1):
            if i not in set_nums:
                # print(i)
                miss = i
                break
        
        for n in nums:

            cnt[n-1] += 1

            if cnt[n-1] == 2:
                duplicat = n

        ans.append(duplicat)
        ans.append(miss)

    
        return ans




