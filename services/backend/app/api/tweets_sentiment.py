from flask_restx import Namespace,Resource
from app.api.crud import get_tweet_sentiment
from flask import jsonify

get_tweet_sentiment_namespace = Namespace("get-tweets")

class GetTweetsSentiment(Resource):
    def get(self):
        tweet_sentiment_json = get_tweet_sentiment()
        return jsonify({"status":"success","message":tweet_sentiment_json})
    
    def post(self):
        return

get_tweet_sentiment_namespace.add_resource(GetTweetsSentiment,"")