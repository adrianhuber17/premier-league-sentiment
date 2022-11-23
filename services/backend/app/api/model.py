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