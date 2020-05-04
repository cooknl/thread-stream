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

tweet ="Unlimited Power! @rakdaddy"  
image_path ="./unlmtd_pwr1.gif" 
  
# to attach the media file 
uploaded = api.media_upload(filename = image_path)
api.update_status(status = tweet, media_ids = [uploaded.media_id])