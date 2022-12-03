from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func


from app import db

class Tweet(db.Model):
    """Tweets table"""

    __tablename__ = "tweets"

    tweets_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date = db.Column(db.DateTime,default=func.now(),nullable=False)
    tweets = db.Column(JSON)

class TweetCount(db.Model):
    """Tweets count table"""

    __tablename__ = "seven_day_tweet_count"

    tweet_count_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date_curr = db.Column(db.DateTime,default=func.now(),nullable=False)
    date_start = db.Column(db.DateTime,nullable=False)
    tweet_count = db.Column(JSON)