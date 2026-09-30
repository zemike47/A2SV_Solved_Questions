class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        left = 0
        right = len(skill) - 1

        size = skill[left] + skill[right]
        total = 0

        while left < right:
            curr_size = skill[left] + skill[right]

            if curr_size != size:
                return -1
            
            product = skill[left] * skill[right]
            total += product

            left += 1
            right -= 1
        
        return total
        


            



