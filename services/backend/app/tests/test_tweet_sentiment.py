import json
from app.helper.constants import DATABASE_INJECTION
from app import db
from app.api.model import Tweet

def test_get_tweet_sentiment(test_app,test_database):
    """testing /get-sentiment with a normal database injection"""
    tweet_sentiment = Tweet(tweets = DATABASE_INJECTION)
    db.session.add(tweet_sentiment)
    db.session.commit()
    client = test_app.test_client()
    resp = client.get("/get-sentiment")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["status"] == "success"
    assert len(data["message"][0]) == 20
    assert "arsenal" in data["message"][0]

def test_get_tweet_count_empty_db(test_app,test_database):
    """testing /get-sentiment with am empy database injection"""
    client = test_app.test_client()
    resp = client.get("/get-sentiment")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert data["status"] == "error"
    assert data["message"] == "database is empty"