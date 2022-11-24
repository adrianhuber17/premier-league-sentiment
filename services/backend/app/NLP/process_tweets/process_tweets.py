
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

# def get_clean_tweets():
#     DATASET_ENCODING = "ISO-8859-1"
#     data = pd.read_csv('NLP/process_tweets/clean_team_tweets.csv', encoding =DATASET_ENCODING)
#     return data

def get_tweet_sentiment(data):
    print("-----Uploading data set-----")
    # #TODO: add data set from tweets after they are clean
    # data = {'text': ["I hate my job", "she sucks","i am great","lets go", "her farts smell bad"]}
    # df = pd.DataFrame(data=data)
    print(data.columns)
    column = data.columns[0]
    X_test = data[column]
    print(f"-----tweet data for {column}-----")
    # print(X_test)
    file_name = "app/NLP/final_model/bernoulli_model.sav"
    file_name_vectorizer = "app/NLP/final_model/vectorizer.sav"
    vectorizer = pickle.load(open(file_name_vectorizer,'rb'))
    loaded_bernoulli_model = pickle.load(open(file_name,'rb'))
    X_test  = vectorizer.transform(X_test)
    y_pred1 = loaded_bernoulli_model.predict(X_test)
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
    return {column:{'positive_tweet_count':count_1,
            'negative_tweet_count':count_0,
            'tweet_count':len(y_pred1)
            }
            }   


# if __name__ == "__main__":
#     data = get_clean_tweets()
#     get_tweet_sentiment(data)