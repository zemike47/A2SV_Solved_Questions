class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        rem_hashmap = defaultdict(int)
        rem_hashmap[0] = 1

        prefixsum = 0
        count = 0

        for i in range(n):
            prefixsum += nums[i]
            rem = prefixsum % k

            if rem < 0:
                rem += k

            if rem in rem_hashmap:
                count += rem_hashmap[rem]
            
            rem_hashmap[rem] += 1

        return count