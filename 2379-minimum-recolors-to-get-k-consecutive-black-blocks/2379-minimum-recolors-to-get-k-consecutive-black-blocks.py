class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        window = {'W':0,'B':0}
        min_ans = float("inf")

        left = 0

        for right in range(len(blocks)):
            window[blocks[right]] += 1


            if right - left + 1 == k:
                min_ans = min(min_ans,window['W'])
                window[blocks[left]] -= 1
                left += 1
        
        return min_ans

                
