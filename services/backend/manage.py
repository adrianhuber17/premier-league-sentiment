#manage.py

import sys, os
from flask.cli import FlaskGroup
from app import create_app,db
from app.api.crud import add_tweet_sentiment,add_seven_day_tweet_count
from app.helper.constants import DATABASE_INJECTION,DATABASE_INJECTION_2,random_injection


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('reset_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("database reset done!")

@cli.command('populate_tweets_db')
def populate_db():
    tweet_sentiment_json = random_injection(DATABASE_INJECTION)
    add_daily_tweet_sentiment = add_tweet_sentiment(tweet_sentiment_json)
    db.session.add(add_daily_tweet_sentiment)
    db.session.commit()
    print("tweets_sentimet_added")

@cli.command('populate_seven_daay_tweets_db')
def populate_db():
    tweet_count_json = DATABASE_INJECTION_2
    tweets_count = add_seven_day_tweet_count(tweet_count_json)
    db.session.add(tweets_count)
    db.session.commit()
    print("seven day tweet count added to db")   

if __name__ == "__main__":
    cli()   