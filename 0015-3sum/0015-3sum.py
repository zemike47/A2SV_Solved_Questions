class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        result = set()

        for i in range(len(nums)-2):
            target = -nums[i]

            hash_set = set()

            for j in range(i+1,len(nums)):
                num = nums[j]
                complment = target - num

                if complment in hash_set:
                    triplet = tuple(sorted([nums[i],num,complment]))
                    result.add(triplet)
                else:
                    hash_set.add(num)

        return [ list(t) for t in result ]

                

                