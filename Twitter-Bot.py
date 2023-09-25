# BUILDING A BASIC "X / Twitter" BOT USING PYTHON : 
import tweepy
import time

# accessing the API authHandler...
auth = tweepy.OAuthHandler(
    "API / Consumer Key here", "API / Consumer Secret here"
)
auth.set_access_token(
    "API / Consumer Key here", "API / Consumer Secret here"
)
api = tweepy.API(auth)

# logging-in the tweepy-bot as 'user'...
user = api.me()

'''Function definition for handling the RateLimitError 
And this method helps to run our program without any crashes(Due to data-rush in twitter server) 
If an error / data-rush occurs, This function is gonna stop the tweepy.cursor for sometime and continue to process when the server becomes free'''
def bound_limiter(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(500) # set delay timer for 500ms...

# function definition to follow back the user -> who follows you :
def follow_back(user_name):
    for follower in bound_limiter(tweepy.Cursor(api.followers).items()):
        if follower.name == 'user_name':
            follower.follow()
        break

# function definition to re-tweet for you name mentioned tweets:
def re_tweet(search_string="--reference_string--", limit=5):
    # as I was using the limit for the items, I don't wanna to set bound-limiter...
    for tweet in tweepy.Cursor(api.search, search_string).items(limit): 
        try:
            tweet.retweet()
            print("Retweeted by @"+str(tweet._json['user']['screen_name'])+" on "+ str(time.ctime()))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

