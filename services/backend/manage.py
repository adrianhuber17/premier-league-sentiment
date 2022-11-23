#manage.py

import sys, os
from flask.cli import FlaskGroup
from app import create_app,db
from app.api.crud import add_tweet_sentiment


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('reset_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("database reset done!")

@cli.command('populate_db')
def populate_db():
    tweet_sentiment_json = {'arsenal':{'positive_tweet_count':10,
                                        'negative_tweet_count':10,
                                        'tweet_count':20
                                        },
                            'chelsea':{'positive_tweet_count':10,
                                        'negative_tweet_count':10,
                                        'tweet_count':20
                                        }
                            }
    add_daily_tweet_sentiment = add_tweet_sentiment(tweet_sentiment_json)
    db.session.add(add_daily_tweet_sentiment)
    db.session.commit()
    print("tweets_sentimet_added")
    
if __name__ == "__main__":
    cli()   