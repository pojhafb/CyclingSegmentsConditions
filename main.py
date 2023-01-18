from src.get_tweets import GetTweetsFromAccounts
from src.config_parser import ConfigParser


def main():

    # Initialize the object with your authentication keys and tokens
    twitter_credentials_cfg = ConfigParser('credentials', 'twitter')
    twitter_credentials = twitter_credentials_cfg.get_credentials('twitter')
    king_county_twitter_settings_cfg = ConfigParser('settings', 'twitter')
    king_county_twitter_settings = king_county_twitter_settings_cfg.get_settings('twitter')

    twitter_data = GetTweetsFromAccounts(twitter_credentials['consumer_key'],
                                         twitter_credentials['consumer_secret'],
                                         twitter_credentials['access_token'],
                                         twitter_credentials['access_token_secret'],
                                         )
    # Get tweets for king co
    tweets = twitter_data.get_tweets(settings=king_county_twitter_settings)
    # Convert king co tweets to a Pandas DataFrame
    twitter_data.tweets_to_dataframe()
    # load tweets_df to table
    twitter_data.load_data_to_tables(settings=king_county_twitter_settings)


if __name__ == '__main__':
    main()
