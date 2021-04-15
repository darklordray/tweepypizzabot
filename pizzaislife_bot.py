import tweepy
import time


print("my twitter bot", flush=True)

CONSUMER_KEY = '***************'
CONSUMER_SECRET = '***************'
ACCESS_KEY = '*******-**********'
ACCESS_SECRET = '************'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
search_results = api.search(q="#******", count=1000)

for result in search_results:
    try:
        print('\nRetweet Bot found tweet by @' + result.user.screen_name + '. ' + 'Attempting to retweet.')

        result.retweet()
        print('Retweet published successfully.')
        time.sleep(900)

    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)
        time.sleep(900)
    
    except StopIteration:
        break
