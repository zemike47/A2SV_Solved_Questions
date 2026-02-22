class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i , j = 0, len(people) - 1
        boats = 0


        while  i <= j:
            if i != j:
                sum_ppl = people[i] + people[j]
                if sum_ppl <= limit:
                    boats += 1
                    i += 1
                    j -= 1
                else:
                    boats += 1
                    j -= 1
            else:
                boats += 1
                i += 1
                
        
           

            
        
        return boats


