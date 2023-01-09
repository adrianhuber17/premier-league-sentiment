
import pickle
#utilities:
import pandas as pd
import numpy as np
import time
# sklearn :
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report


def get_tweet_sentiment(data):
    print("-----Uploading data set-----")
    print(data.columns)
    column = data.columns[2]
    X_test = data[column]
    print(f"-----tweet data for {column}-----")
    # print(X_test)
    print(X_test)
    file_name = "/Users/adrianhuber/football-sentiment/services/backend/app/NLP/final_model/bernoulli_model.sav"
    file_name_vectorizer = "/Users/adrianhuber/football-sentiment/services/backend/app/NLP/final_model/vectorizer.sav"
    vectorizer = pickle.load(open(file_name_vectorizer,'rb'))
    print(vectorizer)
    loaded_bernoulli_model = pickle.load(open(file_name,'rb'))
    X_test  = vectorizer.transform(X_test)
    y_pred1 = loaded_bernoulli_model.predict(X_test)
    print(X_test)
    print(y_pred1)
    count_1 = 0
    count_0 = 0
    for num in y_pred1:
        if num == '0':
            count_0 += 1
        else:
            count_1 += 1
    print(f"-----{column} tweet count = {len(y_pred1)}")
    print('postive_tweet_count: ', count_1)
    print('negative_tweet_count: ', count_0)
    y_df = pd.DataFrame(y_pred1)
    y_df.to_csv("prediction.csv")
    return {column:{'positive_tweet_count':count_1,
            'negative_tweet_count':count_0,
            'tweet_count':len(y_pred1)
            }
            }   

data = pd.read_csv("clean_trump_tweets.csv")
get_tweet_sentiment(data)