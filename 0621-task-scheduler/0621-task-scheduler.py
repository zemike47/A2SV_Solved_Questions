class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        frequency = collections.Counter(tasks)
        
        heap = [(-freq,task) for task, freq in frequency.items() ]

        heapq.heapify(heap)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1

            if cooldown and cooldown[0][1] == time:
                freq,time,task = cooldown.popleft()
                heapq.heappush(heap,(freq,task))
                

            if heap:
                freq, task = heapq.heappop(heap)

                freq += 1

                if freq != 0:
                    cooldown.append((freq,time+n+1,task))
                
        return time 



            





