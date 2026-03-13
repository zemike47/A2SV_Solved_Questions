class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_bills = defaultdict(int)

        for i in range(len(bills)):
            cnt_bills[bills[i]] += 1

            if bills[i] == 10:
                if cnt_bills[5] > 0:
                    cnt_bills[5] -= 1
                else:
                    return False
                
            elif bills[i] == 20:
                if cnt_bills[10] > 0 and cnt_bills[5] > 0:
                    cnt_bills[10] -= 1
                    cnt_bills[5] -= 1
                elif cnt_bills[5] >= 3:
                    cnt_bills[5] -= 3
                
                else:
                    return False
            
        return True






