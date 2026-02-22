class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        i , j = 0 , len(skill) -1 

        total = 0

        common_s = skill[i] + skill[j]

        
            
        print(skill)
        while i <= j:
            s = skill[i] + skill[j]
            c = skill[i] * skill[j]

            if common_s != s:
                return -1

            total += c

            i += 1
            j -= 1
        
        return total
        

        

