
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

def get_tweet_sentiment():
    print("-----Uploading data set-----")
    #TODO: add data set from tweets after they are clean
    data = {'text': ["I hate my job", "she sucks","i am great","lets go", "her farts smell bad"]}
    df = pd.DataFrame(data=data)
    X_test = df["text"]
    print("-----data sample-----")
    print(X_test)
    file_name = "NLP/final_model/bernoulli_model.sav"
    file_name_vectorizer = "NLP/final_model/vectorizer.sav"
    vectorizer = pickle.load(open(file_name_vectorizer,'rb'))
    loaded_bernoulli_model = pickle.load(open(file_name,'rb'))
    X_test  = vectorizer.transform(X_test)
    y_pred1 = loaded_bernoulli_model.predict(X_test)
    print("prediction: ",y_pred1)

if __name__ == "__main__":
    get_tweet_sentiment()