import sqlite3
import tweepy
import pandas as pd


class GetTweetsFromAccounts:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        """
        Initializes a TwitterData object with the given authentication keys and tokens.
        """
        self.tweets_df = None
        self.tweets_obj_list = []
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

        self.data = None

    def get_tweets_from_account(self, settings):
        """
        Returns the specified number of tweets from the given user's timeline.
        """
        screen_names = settings['screen_names']
        count = settings['count']
        for screen_name in screen_names:
            for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=str(screen_name)).items(int(count)):
                self.tweets_obj_list.append(tweet)

    def get_dataframe_from_tweets(self):
        """
        Converts a list of tweets to a Pandas DataFrame.
        """
        self.tweets_df = pd.DataFrame(self.data)
        for tweet in self.tweets_obj_list:
            data = {
                'created_at': tweet.created_at,
                'text': tweet.text,
                'retweet_count': tweet.retweet_count,
                'favorite_count': tweet.favorite_count,
                'screen_name': tweet.user.screen_name,
                'location': tweet.user.location,
            }
            # self.tweets_df = self.tweets_df.append(data, ignore_index=True)
            self.tweets_df = pd.concat([self.tweets_df, pd.DataFrame([data])], ignore_index=True)

    def load_data_to_tables(self, settings):
        conn = sqlite3.connect(settings['database'])
        self.tweets_df.to_sql(settings['table'], conn, if_exists="replace")
        conn.close()
