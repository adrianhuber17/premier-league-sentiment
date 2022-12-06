from flask_restx import Namespace,Resource
from app.api.crud import get_seven_day_tweet_count,add_seven_day_tweet_count
from flask import jsonify
from app.helper.get_tweet_count import GetTweetCount
from app import db

get_tweet_count_namespace = Namespace("get-tweets-count")

class GetTweetsCount(Resource):
    def get(self):

        tweet_count_json = get_seven_day_tweet_count()

        return jsonify({"status":"success","message":tweet_count_json})
    
    def post(self):
        print("-----fetching tweet 7 day count-----")
        get_tweet_count = GetTweetCount().get_team_tweet_count()
        tweets_count = add_seven_day_tweet_count(get_tweet_count)
        db.session.add(tweets_count)
        db.session.commit()
        latest_tweet_count_json = get_seven_day_tweet_count()
        print(latest_tweet_count_json)
        print("seven day tweet count added to db")
        return jsonify({"status:":"success","message":latest_tweet_count_json})

get_tweet_count_namespace.add_resource(GetTweetsCount,"")