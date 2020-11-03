from twitter import Api

class TwitterCrawler:
    
    def __init__(
        self, consumer_key, consumer_secret,
        access_token_key, access_token_secret
    ):
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
        self.access_token_key=access_token_key
        self.access_token_secret=access_token_secret
        self.api=self.create_twitter_api()

    def create_twitter_api(self):
        return Api(
            consumer_key=[self.consumer_key],
            consumer_secret=[self.consumer_secret],
            access_token_key=[self.access_token_key],
            access_token_secret=[self.access_token_secret]
        )

    def search(self):
        pass
