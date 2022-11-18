# utilities : 
import re # regular expression library
import numpy as np
import pandas as pd

# plotting :
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# nltk :
import nltk
from nltk.stem import WordNetLemmatizer

# sklearn :
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

# time library :
import time

# -----Importing the dataset :-----
# DATASET_COLUMNS=['target','ids','date','flag','user','text']
# DATASET_ENCODING = "ISO-8859-1"
# df = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding=DATASET_ENCODING, names=DATASET_COLUMNS)

# # -----Display of the first 5 lines of our dataset :-----
# print(df.head())

# # ----Display the column names of our dataset and additional information :-----
# print(df.columns)
# print(df.shape)
# print(df.info)
# print(df.dtypes)

# # ----Checking for Null values :----
# print(np.sum(df.isnull().any(axis=1)))

# # ----Rows and columns in the dataset :-----
# print('Count of columns in the data is:  ', len(df.columns))
# print('Count of rows in the data is:  ', len(df))

# # -----Checking unique Target Values :-----
# print('unique target values: ',df['target'].unique())
# print('number of unique target values: ', df['target'].nunique())
# print(df.groupby('target').count())


# # -----Plotting the distribution for dataset :-----
# ax = df.groupby('target').count().plot(kind='bar', title='Distribution of data',legend=False)
# # Naming 0 -> Negative , and 4 -> Positive
# ax.set_xticklabels(['Negative','Positive'], rotation=0)
# # Storing data in lists :
# text, sentiment = list(df['text']), list(df['target'])
# plt.show()

# # ----Selecting the text and Target column for our further analysis :---
# data = df[['text','target']]
# # -----Replacing the values to ease understanding :----
# data['target'] = data['target'].replace(4,1)
# # # ----Print unique values of target variable :----
# # print(data['target'].unique())


# # -----Separating positive and negative tweets :-----
# data_pos = data[data['target'] == 1]
# data_neg = data[data['target'] == 0]

# # -----Combining positive and negative tweets :-----
# dataset = pd.concat([data_pos, data_neg])
# # print(dataset['text'].tail())

# # ----Making statement text in lower case :----
# dataset['text'] = dataset['text'].str.lower()
# # print(dataset['text'].tail())

# # -----Defining set containing all stopwords in English :-----
# stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
#                 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before',
#                 'being', 'below', 'between', 'both', 'by', 'can', 'd', 'did', 'do',
#                 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from',
#                 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
#                 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
#                 'into', 'is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
#                 'me', 'more', 'most', 'my', 'myself', 'now', 'o', 'of', 'on', 'once',
#                 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'own', 're',
#                 's', 'same', 'she', "shes", 'should', "shouldve", 'so', 'some', 'such',
#                 't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
#                 'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
#                 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was',
#                 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom',
#                 'why', 'will', 'with', 'won', 'y', 'you', "youd", "youll", "youre",
#                 "youve", 'your', 'yours', 'yourself', 'yourselves']

# # -----Cleaning and removing the above stop words list from the tweet text :-----
# STOPWORDS = set(stopwordlist)


# def cleaning_stopwords(text):
#     return " ".join([word for word in str(text).split() if word not in STOPWORDS])


# dataset['text'] = dataset['text'].apply(lambda text: cleaning_stopwords(text))
# # print(dataset['text'].head())

# #  -----Cleaning and removing punctuations :-----
# import string

# english_punctuations = string.punctuation
# punctuations_list = english_punctuations


# def cleaning_punctuations(text):
#     translator = str.maketrans('', '', punctuations_list)
#     return text.translate(translator)


# dataset['text'] = dataset['text'].apply(lambda x: cleaning_punctuations(x))
# # print(dataset['text'].tail())

# # -----Cleaning and removing repeating characters :-----
# def cleaning_repeating_char(text):
#     return re.sub(r'(.)1+', r'1', text)


# dataset['text'] = dataset['text'].apply(lambda x: cleaning_repeating_char(x))
# # print(dataset['text'].tail())


# # -----Cleaning and removing URL’s :----
# def cleaning_URLs(data):
#     return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)


# dataset['text'] = dataset['text'].apply(lambda x: cleaning_URLs(x))
# # print(dataset['text'].tail())

# # ----Cleaning and removing Numeric numbers :----
# def cleaning_numbers(data):
#     return re.sub('[0-9]+', '', data)
# dataset['text'] = dataset['text'].apply(lambda x: cleaning_numbers(x))
# # print(dataset['text'].tail())

# # -----Getting tokenization of tweet text :----
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# dataset['text'] = dataset['text'].apply(word_tokenize)
# # print(dataset['text'].head())

# #----- Applying Stemming :------
# st = nltk.PorterStemmer()

# def stemming_on_text(data):
#     text = [st.stem(word) for word in data]
#     return data

# dataset['text'] = dataset['text'].apply(lambda x: stemming_on_text(x))
# # print(dataset['text'].head())

# # ----Applying Lemmatizer :----
# lm = nltk.WordNetLemmatizer()

# def lemmatizer_on_text(data):
#     text = [lm.lemmatize(word) for word in data]
#     return data

# dataset['text'] = dataset['text'].apply(lambda x: lemmatizer_on_text(x))
# # dataset['text'].head()

# #----- send all data frames to csv -----
# data.to_csv("data.csv")
# dataset.to_csv("dataset.csv")
# data_neg.to_csv("data_neg.csv")
# data_pos.to_csv("data_pos.csv")

### ---------------------------------------------------------------------------

# --cleaned data processing and model creation


data = pd.read_csv('data.csv')
dataset = pd.read_csv('dataset.csv')
data_neg = pd.read_csv('data_neg.csv')
data_pos = pd.read_csv('data_pos.csv')

# ----Separating input feature and label :----
X = data.text
y = data.target

# # ----Plot a cloud of words for negative tweets :----
# data_neg = data['text'][:800000] # selecting the negative tweets.
# plt.figure(figsize=(20, 20))
# wc_neg = WordCloud(max_words=1000, width=1600, height=800,
#                collocations=False).generate(" ".join(data_neg))
# plt.imshow(wc_neg)
# plt.show()

# # ----Plot a cloud of words for positive tweets :----
# data_pos = data['text'][800000:]  # selecting the positive tweets.
# wc_pos = WordCloud(max_words=1000, width=1600, height=800,
#                collocations=False).generate(" ".join(data_pos))
# plt.figure(figsize=(20, 20))
# plt.imshow(wc_pos)
# plt.show()

# Separating the 95% data for training data and 5% for testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=26105111)

# Fit the TF-IDF Vectorizer :
vectoriser = TfidfVectorizer(ngram_range=(1,2), max_features=500000)
vectoriser.fit(X_train)
# print('No. of feature_words: ', len(vectoriser.get_feature_names()))

# Transform the data using TF-IDF Vectorizer :
X_train = vectoriser.transform(X_train)
X_test  = vectoriser.transform(X_test)
# print(X_test)

