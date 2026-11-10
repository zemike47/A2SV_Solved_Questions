class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []

        answer = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                day = i - stack[-1] 
                answer[stack[-1]] = day
                stack.pop()
            
            stack.append(i)
            
        
        return answer
