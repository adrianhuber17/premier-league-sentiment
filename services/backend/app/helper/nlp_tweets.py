from app.helper.get_tweet_text import GetTweets
from app.NLP.process_tweets.clean_tweet_data import clean_tweet_data
from app.NLP.process_tweets.process_tweets import get_tweet_sentiment
import pandas as pd

def nlp_tweets():
    """fetches tweets for each team last day
    cleans the tweet text data, process machine learnig on data to 
    get sentiment"""

    #get Tweets from twitter by team
    get_tweets = GetTweets()
    get_tweets.get_all_team_tweets_text()
    team_tweets_text = get_tweets.team_tweets_text
    
    sentiments = []
    #clean tweet text
    for team, tweets in team_tweets_text.items():
        curr_team = {team:tweets}
        data = pd.DataFrame.from_dict(curr_team)
        clean_tweets = clean_tweet_data(data)
    
        #process clean tweets with machine learning
        tweet_sentiments = get_tweet_sentiment(clean_tweets)
        sentiments.append(tweet_sentiments)

    return sentiments
    
