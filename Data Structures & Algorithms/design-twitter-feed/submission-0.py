class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append([self.count, tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows[userId] | {userId}
        heap = []
        for f in followees:
            for t, tid in self.tweets[f]:
                heapq.heappush_max(heap, [t, tid])

        res = []
        request = 0
        while heap and request < 10:
            res.append(heapq.heappop_max(heap)[1])
            request += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
