class UndergroundSystem:

    def __init__(self):
        from collections import defaultdict
        self.checkIn_station = defaultdict()
        self.overall = defaultdict(lambda:[0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIn_station[id] = (stationName,t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station,start_time = self.checkIn_station[id]

        end_station = stationName
        end_time = t

        self.overall[(start_station,end_station)][0] += (end_time - start_time)
        self.overall[(start_station,end_station)][1] += 1
    

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.overall[(startStation,endStation)][0] / self.overall[(startStation,endStation)][1] 
    
        



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)