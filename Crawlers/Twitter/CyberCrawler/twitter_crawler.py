from tweepy import (
    OAuthHandler,
    API,
    Cursor,
    error
)
from collections import namedtuple

default_query=" OR ".join([
    "Malware",
    "Ransomware",
    "Advanced Persistent Threat",
    "CVE",
    "Cyber Threat",
])

class TwitterCrawler:
    
    def __init__(
        self, consumer_key, consumer_secret,
        access_token_key, access_token_secret
    ):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token_key=access_token_key
        self.access_token_secret=access_token_secret
        self.api=self.get_api_obj()

    def get_api_obj(self):
        auth=OAuthHandler(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret
        )
        auth.set_access_token(
            self.access_token_key,
            self.access_token_secret
        )

        return API(auth)

    def get_timeline(self):
        public_tweets=self.api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text, end="\n\n\n")

    def search(self, count=200, to_query=default_query):
        try:
            tweets=Cursor(
                self.api.search,
                q=to_query,
                lang="en",
                tweet_mode="extended"
            ).items(count)
        except error.TweepError:
            print(
                color_out("[!!]", "r"),
                "Too many requests have been made... Try again in 10-15 minutes"
            )

        Tweet=namedtuple(
            "Tweet",
            ["created_on", "location", "username", "text"]
        )

        tweets_info=[
            Tweet(t.created_at, t.user.location, t.user.screen_name, t.full_text)
            for t in tweets
        ]

        return tweets_info
        
