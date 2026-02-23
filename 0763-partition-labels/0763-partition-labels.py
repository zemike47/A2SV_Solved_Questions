class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {char:i for i,char in enumerate(s)}

        end = 0
        result = []
        first = 0


        for i,char in enumerate(s):
            end = max(end,last[char])

            if i == end:
                result.append(end - first + 1)
                first = end + 1
                end = 0
            

        return result

            




