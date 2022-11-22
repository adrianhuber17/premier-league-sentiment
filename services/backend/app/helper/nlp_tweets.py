from app.helper.get_tweet_text import GetTweets


get_tweets = GetTweets()
get_tweets.get_all_team_tweets_text()
print(get_tweets.team_tweets_text)
