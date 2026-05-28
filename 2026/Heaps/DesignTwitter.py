class Twitter:

    def __init__(self):
        self.count = 0 # timestamp for most recent tweets, will be negative val for heap
        self.tweetMap = defaultdict(list) # uid -> list [count, tweetIds]
        self.followMap = defaultdict(set) # uid -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]: # get followeeIds and their respective tweets
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # index for every followee's recent post
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap) # put everything in minHeap to get the most recent post
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId) # final product
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index] # put back in heap until the condition is satisfied
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
