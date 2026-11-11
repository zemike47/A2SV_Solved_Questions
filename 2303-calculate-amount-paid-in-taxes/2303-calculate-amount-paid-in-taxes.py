class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:

        tax = 0
        last = 0

        for upper, percent in brackets:

            curr = min(income, upper - last)

            tax += curr * percent / 100

            income -= curr
            last = upper

            if income == 0:
                break

        return tax