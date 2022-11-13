import requests
import os

os.environ.get()
twitter_endpoint = "https://api.twitter.com/2/tweets/counts/recent"
headers = {"Authorization":""}
r = requests.get(twitter_endpoint,headers=headers)

