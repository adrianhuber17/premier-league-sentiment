from flask_restx import Namespace,Resource
from app.api.crud import get_tweet_sentiment,add_tweet_sentiment
from flask import jsonify
from app.helper.nlp_tweets import nlp_tweets
from app import db

get_tweet_sentiment_namespace = Namespace("get-tweets")

class GetTweetsSentiment(Resource):
    def get(self):
        tweet_sentiment_json = get_tweet_sentiment()
        if not tweet_sentiment_json[0] or not tweet_sentiment_json[1]:
            response = jsonify({"status":"error","message":"database is empty"})
            response.status_code = 404
            return response
        response =jsonify({"status":"success","message":tweet_sentiment_json})
        response.status_code = 200
        return response
    
    def post(self):
        tweet_sentiments = nlp_tweets()
        print("-----sentiment going into the database-----")
        print(tweet_sentiments)
        add_daily_tweet_sentiment = add_tweet_sentiment(tweet_sentiments)
        db.session.add(add_daily_tweet_sentiment)
        db.session.commit()
        print("tweets sentimet added")
        response = jsonify({"status:":"success","message":tweet_sentiments})
        response.status_code = 201
        return response

get_tweet_sentiment_namespace.add_resource(GetTweetsSentiment,"")