class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners = {}
        losers = {}

        for match in matches:
            winners[match[0]] = winners.get(match[0],0) + 1
            losers[match[1]] = losers.get(match[1],0) + 1

        
        answer = [[],[]]

        winners = dict(sorted(winners.items()))
        losers = dict(sorted(losers.items()))


        for winner in winners.keys():
            if winner not in losers.keys():
                answer[0].append(winner)
        
        for loser in losers.items():
            if loser[1] == 1:
                answer[1].append(loser[0])

        

        return answer


        


        


        