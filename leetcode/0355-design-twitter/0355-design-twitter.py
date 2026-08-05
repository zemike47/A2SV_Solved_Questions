class Twitter:

    def __init__(self):
        self.usermap = defaultdict(set)
        self.tweetmap = defaultdict(list)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.usermap[userId] | {userId}

        heap = []

        for user in users:
            if self.tweetmap[user]:
                index = len(self.tweetmap[user]) - 1

                time , tweetId = self.tweetmap[user][index]

                heapq.heappush(heap,(-time,tweetId,user,index))

        
        result = []

        while heap and len(result) < 10:
            time,tweetId,user,index = heapq.heappop(heap)

            result.append(tweetId)
            index -= 1

            if index >= 0:
                time , tweetId = self.tweetmap[user][index]

                heapq.heappush(heap,(-time,tweetId,user,index))

        return result




    def follow(self, followerId: int, followeeId: int) -> None:
        self.usermap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usermap[followerId].discard(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)