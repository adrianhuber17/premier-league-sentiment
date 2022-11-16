import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')

search_url = "https://api.twitter.com/2/tweets/search/recent"
teams = ["chelsea fc","manchester city"]

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(search_url, params,team_tweets,team):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response_json = response.json()
    if team not in team_tweets:
        team_tweets[team] = []
    team_tweets[team].append(response_json['data'])
    if 'next_token' in response_json['meta']:
        query_params = {'query': f"\"{team}\" lang:en -is:retweet",
                        'start_time': '2022-11-14T00:00:00.000Z',
                        'max_results':100,
                        'next_token':response_json['meta']['next_token']
                        }
        connect_to_endpoint(search_url, query_params,team_tweets,team)

    return team_tweets


def get_team_tweets(teams):
    team_tweets = {}
    for team in teams:
        query_params = {'query': f"\"{team}\" lang:en -is:retweet",
                        'start_time': '2022-11-14T00:00:00.000Z',
                        'max_results':100,
                        }
        connect_to_endpoint(search_url, query_params,team_tweets,team)

    return team_tweets

team_tweets = get_team_tweets(teams)

team_tweets_text = {}
for team, tweets in team_tweets.items():
    for tweet_batch in tweets:
        for text in tweet_batch:
            if team not in team_tweets_text:
                team_tweets_text[team] = []
            print(text['text'])
            team_tweets_text[team].append(text['text'])

team_tweets_df = pd.DataFrame.from_dict(team_tweets_text,orient='index').T
print(team_tweets_df.head(10))
team_tweets_df.to_csv("team_tweets.csv")