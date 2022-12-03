from flask_restx import Namespace,Resource
from app.api.crud import get_tweet_sentiment,add_tweet_sentiment
from flask import jsonify
from app.helper.nlp_tweets import nlp_tweets
from app import db

get_tweet_count_namespace = Namespace("get-tweets-count")

class GetTweetsCount(Resource):
    #TODO: after model is created in the database, create end points
    def get(self):
        tweet_sentiment_json = get_tweet_sentiment()
        return jsonify({"status":"success","message":tweet_sentiment_json})
    
    # def post(self):
    #     tweet_sentiments = nlp_tweets()
    #     print("-----sentiment going into the database-----")
    #     print(tweet_sentiments)
    #     add_daily_tweet_sentiment = add_tweet_sentiment(tweet_sentiments)
    #     db.session.add(add_daily_tweet_sentiment)
    #     db.session.commit()
    #     print("tweets sentimet added")
    #     return tweet_sentiments, 200

get_tweet_count_namespace.add_resource(GetTweetsCount,"")