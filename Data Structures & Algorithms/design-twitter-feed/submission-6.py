class Twitter:

    def __init__(self):
        self.count = 0
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append((self.count, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.follows[userId] | {userId}
        heap = []
        for f in followers:
            heap.extend(self.tweets.get(f, []))
        heapq.heapify_max(heap)

        res = []
        while len(res) < 10 and heap:
            res.append(heapq.heappop_max(heap))

        return [tweet_id for _, tweet_id in res]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
