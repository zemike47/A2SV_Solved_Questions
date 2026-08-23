class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        total = 0
        digits= digits[::-1]
        

        while len(digits) > 0:
            r = digits.pop()
            total = total * 10 + r

        n = total
        n += 1
        print(n)

        result = []

        while n > 0:
            r = n % 10
            result.append(r)
            n //= 10

        return result[::-1]

        