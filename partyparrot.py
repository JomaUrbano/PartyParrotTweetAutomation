import tweepy
import credentials
import os
import time
import random

# APIs and connection to twitter page
def twitter_api():
    
    credentials.ACCESS_KEY
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

# Randomizes a parrot from parrots folder, returns a path
def chosenParrot():
  parrots = os.listdir('./parrots/hd/')
  return "./parrots/hd/{}".format(parrots[random.randint(0,len(parrots)-1)])

status = ""


# Tweets a randomed parrot every hour
while True:
  twitter_api().update_with_media(chosenParrot(), status)
  time.sleep(1800) 


