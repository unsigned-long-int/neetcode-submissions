class Twitter:

    def __init__(self):
        self.count = 0
        self.follows = defaultdict(set)
        self.tweets = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].add((self.count, tweetId))

        
    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows[userId] | {userId}

        heap = []
        for follow in followees:
            heap.extend([tweet for tweet in self.tweets[follow]])
        heapq.heapify_max(heap)
        i = 0
        res = []
        while heap and i < 10:
            i += 1
            res.append(heapq.heappop_max(heap)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

