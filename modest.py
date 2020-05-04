from threader import Threader
from itertools import chain
import tweepy
import textwrap
import os

with open("mod_prop_min.txt","r") as f:
    full_text = f.read()

paragraphs_no_n = [p.replace("\n"," ") for p in full_text.split("\n\n")]

wrapped = list(chain.from_iterable([textwrap.wrap(p,270) for p in paragraphs_no_n]))

t = len(wrapped)
wrapped_n = [ l + f'  [{n+1}/{t}]' for n, l in enumerate(wrapped)]

with open('mod_prop_tweetable.txt', 'wt') as f:
    f.writelines(l + '\n' for l in wrapped_n)

with open('mod_prop_tweetable.txt') as f:
    wrapped_n = [line.rstrip() for line in f]

# personal details
consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_SECRET_KEY")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = [f"A MODEST THREAD   [0/{t}]"]
tweets.extend(wrapped_n)

username = None
th = Threader(tweets, api, wait=1, user=username, end_string=False)
print(th)

th.send_tweets() # This where is gets to the real world.

