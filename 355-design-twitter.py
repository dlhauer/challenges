from datetime import datetime
class Twitter:

    def __init__(self):
        self.tweets = []
        self.users = dict()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append({
            'user_id': userId,
            'tweet_id': tweetId,
            'date': datetime.now()
        })
        

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        

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

twitter = Twitter()
twitter.postTweet(1,1)
twitter.postTweet(1,2)
twitter.follow(1,2)
twitter.follow(1,3)
twitter.follow(2,1)
twitter.unfollow(1,3)

print(twitter.users)