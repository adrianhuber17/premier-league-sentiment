import json
from app.helper.constants import DATABASE_INJECTION_2
from app import db
from app.api.model import TweetCount

def test_get_tweet_count(test_app,test_database):
    tweet_count = TweetCount(date_start=DATABASE_INJECTION_2[-1],tweet_count=DATABASE_INJECTION_2[0])
    db.session.add(tweet_count)
    db.session.commit()
    client = test_app.test_client()
    resp = client.get("/get-tweet-count")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["status"] == "success"
    assert data["message"]["start_date"] == "Sat, 26 Nov 2022 22:53:34 GMT"

def test_get_tweet_count_empty_db(test_app,test_database):

    client = test_app.test_client()
    resp = client.get("/get-tweet-count")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["status"] == "success"
    assert data["message"] == {}