from flask_restx import Api
from app.api.ping import ping_namespace
from app.api.get_tweets import get_tweet_namespace

api = Api(version="1.0", title="APIs", doc="/docs/")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(get_tweet_namespace,"/get-sentiment")