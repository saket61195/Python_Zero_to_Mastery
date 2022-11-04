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
id = user.id_str
print(id)
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)