import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd

class GetTweets:

    def __init__(self):
        load_dotenv()
        self.bearer_token = os.getenv('BEARER_TOKEN')
        self.search_url = "https://api.twitter.com/2/tweets/search/recent"
        self.teams = ["chelsea fc","manchester city"] # change to constants
        self.team_tweets = {}
        self.team_tweets_text = {}

    def get_all_team_tweets_text(self):
        self.__get_all_team_tweets()
        for team, tweets in self.team_tweets.items():
            for tweet_batch in tweets:
                for text in tweet_batch:
                    if team not in self.team_tweets_text:
                        self.team_tweets_text[team] = []
                    self.team_tweets_text[team].append(text['text'])
                    
        #create df from team tweets
        team_tweets_df = pd.DataFrame.from_dict(self.team_tweets_text,orient='index').T
        print(team_tweets_df.head(10))
        team_tweets_df.to_csv("team_tweets.csv")
            
    def __get_all_team_tweets(self):

        for team in self.teams:
            query_params = {'query': f"\"{team}\" lang:en -is:retweet",
                            'start_time': '2022-11-14T00:00:00.000Z',
                            'max_results':100,
                            }
            self.__connect_to_endpoint(query_params,team)
    
    def __bearer_oauth(self,r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r
        
    def __connect_to_endpoint(self, params,team):
        response = requests.request("GET", self.search_url, auth=self.__bearer_oauth, params=params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        response_json = response.json()
        if team not in self.team_tweets:
            self.team_tweets[team] = []
        self.team_tweets[team].append(response_json['data'])
        if 'next_token' in response_json['meta']:
            query_params = {'query': f"\"{team}\" lang:en -is:retweet",
                            'start_time': '2022-11-14T00:00:00.000Z',
                            'max_results':100,
                            'next_token':response_json['meta']['next_token']
                            }
            self.__connect_to_endpoint(query_params,team)
    

get_tweets = GetTweets()
get_tweets.get_all_team_tweets_text()
