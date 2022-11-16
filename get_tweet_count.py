import requests
import os
import json
from dotenv import load_dotenv
from constants import premier_league_teams

load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')

search_url = "https://api.twitter.com/2/tweets/counts/recent"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r


def connect_to_endpoint(search_url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_team_tweet_count():
    team_tweets_count = {}
    for team in premier_league_teams:
        query_params = {'query': f"\"{team}\" lang:en -is:retweet",'start_time': '2022-11-14T00:00:00.000Z'}
        json_response = connect_to_endpoint(search_url, query_params)
        total_tweet_count = json_response["meta"]
        team_tweets_count[team] = total_tweet_count
        # print(json.dumps(json_response, indent=4, sort_keys=True))
    return team_tweets_count


team_tweets_count = get_team_tweet_count()
rank = []
for team,total_tweet_count in team_tweets_count.items():
    rank.append((team,total_tweet_count['total_tweet_count']))

rank.sort(key=lambda y:y[1],reverse=True)
print(rank)