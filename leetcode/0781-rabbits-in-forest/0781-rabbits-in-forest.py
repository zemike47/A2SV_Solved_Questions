class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)

        ans = 0

        for k , c in cnt.items():
            group = k + 1
            group_size = math.ceil(c / group)

            ans  += group * group_size

        return ans