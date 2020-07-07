from datetime import datetime

class Twitter:

    def __init__(self):
        self.tweets = []
        self.users = dict()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {'following': set()}
        self.tweets.append({
            'user_id': userId,
            'tweet_id': tweetId,
            'date': datetime.now()
        })
        

    def getNewsFeed(self, userId: int) -> list:
        if userId not in self.users:
            return []
        news_feed = sorted([t for t in self.tweets 
                     if t['user_id'] == userId
                     or t['user_id'] in self.users[userId]['following']],
                     reverse=True,
                     key=lambda x: x['date'])
        return [t['tweet_id'] for t in news_feed][:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if type(followerId) is not int or type(followeeId) is not int:
            return None
        if followerId not in self.users:
            self.users[followerId] = {'following': {followeeId}}
        else:
            self.users[followerId]['following'].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if type(followerId) is not int or type(followeeId) is not int:
            return None
        if (followerId not in self.users 
            or followeeId not in self.users[followerId]['following']):
            return
        self.users[followerId]['following'].remove(followeeId)
