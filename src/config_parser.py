import configparser
from typing import Union


class ConfigParser:
    settings: dict[str, Union[str, list[str]]]
    credentials: dict[str, str]

    def __init__(self, cfg_type, platform):
        self.config = configparser.ConfigParser()
        if cfg_type == 'credentials':
            self.config.read('../config/src/credentials.cfg')
            self.credentials = None
            if platform == 'twitter':
                self.consumer_key = None
                self.consumer_secret = None
                self.access_token = None
                self.access_token_secret = None
        elif cfg_type == 'settings':
            self.config.read('../config/src/settings.cfg')
            self.settings = None
            if platform == 'twitter':
                self.count = None
                self.screen_names = None
                self.table_name = None

    def get_credentials(self, platform):
        if platform == 'twitter':
            # Read values from the 'Twitter API' section
            self.consumer_key = self.config['Twitter']['consumer_key']
            self.consumer_secret = self.config['Twitter']['consumer_secret']
            self.access_token = self.config['Twitter']['access_token']
            self.access_token_secret = self.config['Twitter']['access_token_secret']
            self.credentials = {'consumer_key': self.consumer_key,
                                'consumer_secret': self.consumer_secret,
                                'access_token': self.access_token,
                                'access_token_secret': self.access_token_secret,
                                }
        return self.credentials

    def get_settings(self, channel):
        if channel == 'King_County_Twitter':
            # Read values from the 'Twitter API' section
            self.count = self.config['KingCountyTwitter']['count']
            self.screen_names = self.config['KingCountyTwitter']['screen_names'].split(',')
            self.table_name = self.config['KingCountyTwitter']['table_name']
            self.settings = {'count': self.count,
                             'screen_names': self.screen_names,
                             'table_name': self.table_name,
                             }
        return self.settings
