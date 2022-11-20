
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

# data = {'text': ["great", "bad"]}
# X_test = pd.DataFrame(data=data)
# print(X_test)
# vectoriser = TfidfVectorizer(ngram_range=(1,2), max_features=None)
# print(vectoriser)
# vectoriser.fit(X_test)
# X_test  = vectoriser.transform(X_test)
# print(X_test)
# file_name = "NLP/bernoulli_model.sav"
# # load model
# loaded_bernoulli_model = pickle.load(open(file_name,'rb'))
# y_pred1 = loaded_bernoulli_model.predict(X_test)
# print(y_pred1)
# # print(loaded_bernoulli_model.score(X_test,y_test))