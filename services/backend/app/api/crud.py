"""CRUD operations"""

from app import db
from app.api.model import Tweet
from sqlalchemy import desc
from flask import jsonify

def add_tweet_sentiment(tweets_sentiment_json):
    """adds daily tweet sentiment to database"""

    tweet_sentiment = Tweet(tweets = tweets_sentiment_json)

    return tweet_sentiment

def get_tweet_sentiment():
    """gets latest tweet sentiments"""

    tweet_sentiment = db.session.query(Tweet).order_by(Tweet.date).limit(7)
    tweet_sentiment_json = {}
    for sentiment_info in tweet_sentiment:
        
        date = sentiment_info.date
        id = sentiment_info.tweets_id
        
        for tweet in sentiment_info.tweets:
            for team, sentiment in tweet.items():
                if team not in tweet_sentiment_json:
                    tweet_sentiment_json[team] = []
                tweet_sentiment_json[team].append(sentiment['positive_percentage'])

    return tweet_sentiment_json

