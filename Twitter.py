##Stock Movement Analysis Based on Social Media Sentiment in Twitter

#Python Code

import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'uXMSy98NAEA1YiPiNBfmBjsjx'
consumer_key_secret = 'orp6sZjAG1jZvwIngE4mCudl7aoHwF0X7HachWHnJ7ik1bmmWZ'
access_token = '1864253945364750336-LoWRG10XhQgC5UK81M43RxLDThSWhj'
access_token_secret = 'kG9VvNcNXEfbc3SDz2oc3z5HuKMp98NgqPE6ZRdurcubB'

# Authenticate with the Twitter API
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAFdtxQEAAAAAfPUKo%2F7LF3ngHHQ%2Fhp8Zv2w5Fos%3DVO7Ewa6YxJ34x3jnArTv1DgSSLJJPam4fH3LWmvw84FXCecq5B",  # Required for v2
    consumer_key=consumer_key,
    consumer_secret=consumer_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Query for recent tweets
query = "HEG"  # Replace with your search term
tweets = client.search_recent_tweets(
    query=query,
    max_results=10,  # Maximum results to fetch (10–100)
    tweet_fields=["text", "lang"]  # Additional tweet fields
)

# Process the tweets
if tweets.data:
    for tweet in tweets.data:
        if tweet.lang == "en":  # Ensure it's an English tweet
            print(tweet.text)
            analysis = TextBlob(tweet.text)
            print("Sentiment Analysis:", analysis.sentiment)

            # Determine polarity
            if analysis.sentiment.polarity > 0:
                print("Positive")
            elif analysis.sentiment.polarity < 0:
                print("Negative")
            else:
                print("Neutral")
else:
    print("No tweets found.")



