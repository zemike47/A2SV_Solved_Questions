class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                last = stack.pop()

                if last == 0:
                    score = 1
                else:
                    score = 2 * last

                stack[-1] += score

        return stack[-1]

                




        

