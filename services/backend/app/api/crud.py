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

    tweet_sentiment = db.session.query(Tweet).order_by(desc(Tweet.date)).limit(7)
    tweet_sentiment_json = {}
    for sentiment_info in tweet_sentiment:
        tweet_sentiment_json[sentiment_info.tweets_id] = {'tweets_id':sentiment_info.tweets_id,
                                                        'tweets_sentiment':sentiment_info.tweets,
                                                        'date':sentiment_info.date}

    return tweet_sentiment_json

