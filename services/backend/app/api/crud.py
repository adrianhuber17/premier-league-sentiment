"""CRUD operations"""

from app import db
from app.api.model import Tweet
from sqlalchemy import desc

def add_tweet_sentiment(tweets_sentiment_json):
    """adds daily tweet sentiment to database"""

    tweet_sentiment = Tweet(tweets = tweets_sentiment_json)

    return tweet_sentiment