class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        radius = 0
        heaters.sort()

        for house in houses:
            min_dis = float("inf")
            left , right = 0 , len(heaters) - 1
            
            while left <= right:
                mid = (left + right) // 2

                # if heaters[mid] ==  houses[i]:
                #     min_dis = min(min_dis,abs(houses[i]-heaters[mid]))
                #     break
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            dist1 = float("inf") if left >= len(heaters) else abs(heaters[left] - house)
            dist2 = float("inf") if right < 0 else abs(heaters[right] - house)
            
            min_dis = min(dist1,dist2)

            radius = max(radius,min_dis)

        return radius

            


        

    





        # uncoverd = set(houses) - set(heaters)
        # r = 0

        # ranges  = [ [h,h] for h in heaters]
        # # print(radius)

        # while uncoverd:
        #     r += 1

        #     for rng in ranges:
        #         rng[0] -= 1
        #         rng[1] += 1

        #         if rng[0] in uncoverd:
        #             uncoverd.remove(rng[0])
        #         if rng[1] in uncoverd:
        #             uncoverd.remove(rng[1])

        # return r


