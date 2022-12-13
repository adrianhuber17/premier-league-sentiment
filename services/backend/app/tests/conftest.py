import pytest
from app import create_app,db
from app.api.model import Tweet,TweetCount

@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("app.config.TestingConfig")
    with app.app_context():
        yield app

@pytest.fixture(scope="function")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope="function")
def add_tweet():
    def _add_tweet():
        pass