class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])

            else:
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
        
                k = ""

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                k = int(k)
                stack.append(k*substring)

        return "".join(stack)

