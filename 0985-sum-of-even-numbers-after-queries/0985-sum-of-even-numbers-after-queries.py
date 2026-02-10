class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []
        sum_of_even_nums  = 0

        for num in nums:
            if num % 2 == 0:
                sum_of_even_nums += num
        
       
        for vali, indexi in queries:
            if nums[indexi] % 2 == 0:
                sum_of_even_nums -= nums[indexi]
            
            nums[indexi] += vali

            if nums[indexi] % 2 == 0:
                sum_of_even_nums += nums[indexi]

            ans.append(sum_of_even_nums)      
           

        return ans





        
        














