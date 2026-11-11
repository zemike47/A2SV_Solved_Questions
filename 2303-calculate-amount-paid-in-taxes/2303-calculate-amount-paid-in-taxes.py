class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        
        tax = 0
        last = 0

        for upper , percent in brackets:
            if income <= 0:
                break
            
            if upper - last >= income:
                curr = income
            else:
                curr = upper - last
            
            tax += (curr * (percent / 100))

            income -= curr
            last = upper
        
        return tax
