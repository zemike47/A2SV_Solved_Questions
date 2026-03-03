class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        rem_map = {0:-1}
        prefixsum = 0

        for i in range(len(nums)):
            prefixsum += nums[i]
            rem = prefixsum % k

            if rem < 0:
                rem += k
            
            if rem in rem_map:
                if i - rem_map[rem] >= 2:
                    return True
            else:
                rem_map[rem] = i
            
        else:
            return False

       

            
            

