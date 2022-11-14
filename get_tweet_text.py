import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')

search_url = "https://api.twitter.com/2/tweets/search/recent"
team = "chelsea fc"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r


def connect_to_endpoint(search_url, params,tweet_texts):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response_json = response.json()
    tweet_texts.append(response_json['data'])

    if 'next_token' in response_json['meta']:
        query_params = {'query': team,
                        'start_time': '2022-11-13T00:00:00.000Z',
                        'max_results':100,
                        'next_token':response_json['meta']['next_token']}
        connect_to_endpoint(search_url, query_params,tweet_texts)

    return tweet_texts


def get_tweets_text(team):
    tweet_texts = []
    query_params = {'query': team,
                    'start_time': '2022-11-13T00:00:00.000Z',
                    'max_results':100}
    tweet_texts = connect_to_endpoint(search_url, query_params,tweet_texts)
    return tweet_texts


tweets_text = get_tweets_text(team)
# print(tweets_text)
print(len(tweets_text))