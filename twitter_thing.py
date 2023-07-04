import tweepy
from datetime import datetime, timedelta

# Replace these with your own credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Calculate the date one week ago
one_week_ago = datetime.now() - timedelta(weeks=1)

# Get all tweets from your timeline
for status in tweepy.Cursor(api.user_timeline).items():
    # Check if the tweet is older than one week
    if status.created_at < one_week_ago:
        # Delete the tweet
        api.destroy_status(status.id)