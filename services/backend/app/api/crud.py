"""CRUD operations"""

from app import db
from app.api.model import Tweet,TweetCount
from sqlalchemy import desc
from flask import jsonify

def get_seven_day_tweet_count():
    """get 7 days tweet counts for all teams"""

    tweet_count = db.session.query(TweetCount).order_by(desc(TweetCount.date_curr)).first()
    tweet_count_json = {'curr_date':tweet_count.date_curr,
                        'start_date':tweet_count.date_start,
                        'tweet_count':tweet_count.tweet_count}
    
    return tweet_count_json

def add_seven_day_tweet_count(tweets_count_json):
    """adds total tweet count for the last 7 days for each team"""

    count = tweets_count_json[0]
    date_start = tweets_count_json[1]

    tweets_count = TweetCount(date_start=date_start,tweet_count=count)

    return tweets_count

def add_tweet_sentiment(tweets_sentiment_json):
    """adds daily tweet sentiment to database"""

    tweet_sentiment = Tweet(tweets = tweets_sentiment_json)

    return tweet_sentiment

def get_tweet_sentiment():
    """gets latest tweet sentiments"""

    tweet_sentiment = db.session.query(Tweet).order_by(desc(Tweet.date)).limit(7)
    tweet_sentiment_json = {}
    dates = []
    for sentiment_info in tweet_sentiment:
        
        date = sentiment_info.date
        id = sentiment_info.tweets_id
        dates.append(date)
        for tweet in sentiment_info.tweets:
            for team, sentiment in tweet.items():
                if team not in tweet_sentiment_json:
                    tweet_sentiment_json[team] = []
                tweet_sentiment_json[team].append((sentiment['positive_percentage']))

    response_json = [tweet_sentiment_json,dates]
    return response_json

