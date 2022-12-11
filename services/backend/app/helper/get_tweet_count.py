import requests
import os
import json
from dotenv import load_dotenv
from app.helper.constants import PREMIER_LEAGUE_TEAMS
from datetime import datetime,timedelta

class GetTweetCount:

    def __init__(self):
        load_dotenv()
        self.bearer_token = os.getenv('BEARER_TOKEN')
        self.seven_day_range = (datetime.utcnow()- timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        print("fetch time -1 days: ",self.seven_day_range)
        self.search_url = "https://api.twitter.com/2/tweets/counts/recent"
        self.teams = PREMIER_LEAGUE_TEAMS
        self.team_tweets_count = {}
        self.team_tweets_count_rank = []
    
    def get_team_tweet_count(self):
        for team in PREMIER_LEAGUE_TEAMS:
            query_params = {'query': f"\"{team}\" lang:en -is:retweet",'start_time': self.seven_day_range}
            json_response = self.__connect_to_endpoint(self.search_url, query_params)
            total_tweet_count = json_response["meta"]
            self.team_tweets_count[team] = total_tweet_count

        self.__rank_tweet_count()

        return [self.team_tweets_count_rank,datetime.utcnow()- timedelta(days=1)]

    def __rank_tweet_count(self):
        for team,total_tweet_count in self.team_tweets_count.items():
            self.team_tweets_count_rank.append((team,total_tweet_count['total_tweet_count']))

        self.team_tweets_count_rank.sort(key=lambda y:y[1],reverse=True)

    def __bearer_oauth(self,r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "v2RecentTweetCountsPython"
        return r

    def __connect_to_endpoint(self,search_url, params):
        response = requests.request("GET", search_url, auth=self.__bearer_oauth, params=params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
