# A Modest Twitter Thread

## Content

http://www.gutenberg.org/files/1080/1080-0.txt

Downloaded using `curl`, but didn't have `curl`, so

```bash
sudo apt get install curl
```

Then
```bash
curl http://www.gutenberg.org/files/1080/1080-0.txt > mod_prop.txt
```

## `mod_prop_min.txt`

Manually remove all the preamble and post-matter, including title and author.

## Conversion to tweet-size lines

Read in full text

```python
with open("mod_prop_min.txt","r") as f:
    full_text = f.read()
```

Split by `\n\n` to get paragraphs preserved.

```python
paragraphs = full_text.split("\n\n")
```

Then replace newlines within paragraphs by spaces.

```python
paragraphs_no_n = [p.replace("\n"," ") for p in paragraphs]
```

Now to divide into 270 character chunks. `textwrap()` and `chain()` to the rescue!

```python
import textwrap
from itertools import chain
wrapped = list(chain.from_iterable([textwrap.wrap(p,270) for p in paragraphs_no_n]))
```

Let's add "1/n" to the end of each line

```python
t = len(wrapped)
wrapped_n = [ l + f'{n+1}/{t}' for n, l in enumerate(wrapped)]
```

Let's write it to a file for safe keeping

```python
with open('mod_prop_tweetable.txt', 'wt') as f:
    f.writelines(l + '\n' for l in wrapped_n)
```

This is how to read it back in without newline characters

```python
with open('mod_prop_tweetable.txt') as f:
    wrapped_n = [line.rstrip() for line in f]
```

## `excode`

Small diversion to modify `excode` package to make test bundling optional.

https://github.com/cooknl/excode

## The Twitter API

https://developer.twitter.com/en/apps

https://www.geeksforgeeks.org/tweet-using-python/

When setting up the app, don't Enable Log in

https://stackoverflow.com/questions/50601607/twitter-call-back-url

This is not straightforward

https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0

But don't put spaces around your equal signs! Or hyphens in your identifiers!

https://stackoverflow.com/questions/18042369/bash-export-not-a-valid-identifier

```python
# importing the module
import tweepy
import os

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

# update the status
api.update_status(status ="Hello Everyone !")

```

Success!

## Thread Building

https://github.com/choldgraf/threader

Unfortunately threader requires `TwitterAPI`

Now I get to alter another open source project!

Time to fork...

Everything's fine until this point

```
            # Send POST and get response
            resp = self.api.request('statuses/update', params=params)
```

Turns out `tweepy` has a different way to update status and package responses than TwitterAPI

https://github.com/geduldig/TwitterAPI

I flirted with the idea of changing to a different library than tweepy, including embracing TwitterAPI, but the docs are better (though still incomplete) and tweepy is a more maintained library, so I stuck with tweepy.

https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries


## Bringing it together

```python
import tweepy
from threader import Threader
import os

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

username = None
tweets = ["OK this should work now", "does it work?! is it threaded?!", "maybe........", "fingers crossed!"]
th = Threader(tweets, api, wait=1, user=username, end_string=False)
th

# th.send_tweets() # This where is gets to the real world.
```