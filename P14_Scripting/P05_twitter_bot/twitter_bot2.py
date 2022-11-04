import tweepy

consumer_key = 'cb76GAAruFBNecB3mBe7xddLc'
consumer_secret = '9nHShs7EWB2Crvjbm5V8gsfYzysHicXfHzKId3nvnLbS5PVp9O'
access_token = '1510217461961924609-U7dAlMKoM8LgBerpu7mP6eKQsGBdIx'
access_token_secret = 'qxpuk5clH4UxpLHVC71XJgNg7zTR2h20ydb1JL7lWL9at'


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)
user = api.get_user(screen_name='saket61195')


search_string = "python"
numberOfTweets = 1

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numberOfTweets):
    # try:
    #     tweet.favorite()
    #     print('i like the tweet')
    #   #   tweet.retweet()
    # except tweepy.TweepyException as e:
    #     print(e)
    # except StopIteration:
    #     break
    pass


