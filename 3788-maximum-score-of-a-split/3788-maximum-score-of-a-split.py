class Solution:
    def maximumScore(self, nums: List[int]) -> int:
    
        
        prefixArr = [0] * len(nums)
        
        prefixArr[0] = nums[0]
        
        for i in range(1,len(nums)):
            
            prefixArr[i] = prefixArr[i-1] + nums[i]
            
        sufixMin = [0] * len(nums)
        sufixMin[len(nums)-1] = nums[-1]
        
        for i in range(len(nums)-2,-1,-1):
            sufixMin[i] = min(nums[i],sufixMin[i+1])
            
        score = [0] * (len(nums) - 1)
        
        for i in range(len(nums)-1):
            score[i] = prefixArr[i] - sufixMin[i+1]
            
        #print(prefixArr)
        #print(sufixMin)
        #print(score)
        #print("---")
        
        
        return max(score)