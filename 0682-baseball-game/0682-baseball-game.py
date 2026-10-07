class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if stack and op == '+':
                new_record = stack[-1] + stack[-2]

                stack.append(new_record)
            
            elif stack and op == 'D':
                new_record = stack[-1]

                stack.append(2 * new_record)
            
            elif stack and op == 'C':
                stack.pop()

            else:
                new_record = int(op)

                stack.append(new_record)
            
        return sum(stack)
            








