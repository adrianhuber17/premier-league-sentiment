import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')

search_url = "https://api.twitter.com/2/tweets/counts/recent"

# Optional params: start_time,end_time,since_id,until_id,next_token,granularity
query_params = {'query': 'chelsea fc','start_time': '2022-11-07T00:00:00.000Z'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r


def connect_to_endpoint(search_url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()