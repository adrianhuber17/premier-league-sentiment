from flask_restx import Namespace,Resource
from app.api.crud import get_tweet_sentiment
from flask import jsonify

get_tweet_namespace = Namespace("get-tweets")

class GetTweets(Resource):
    def get(self):
        tweet_sentiment_json = get_tweet_sentiment()
        print(tweet_sentiment_json)
        return jsonify({"status":"success","message":tweet_sentiment_json})

get_tweet_namespace.add_resource(GetTweets,"")