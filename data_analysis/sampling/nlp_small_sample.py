## imports ##
# utilities : 
import re 
import numpy as np
import pandas as pd
import string

# plotting :
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# nltk :
# import nltk
# from nltk.stem import WordNetLemmatizer,PorterStemmer
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
# from nltk.corpus import stopwords

# import new data
columns = ["target","number","date","query","user","text"]
df = pd.read_csv("/Users/adrianhuber/football-sentiment/services/backend/app/NLP/train_model/training_data_set.csv",encoding_errors='ignore')
df.columns = columns

# filtered data for text and target
raw_data_df = df[["target","text"]]

# df for negative and positive data
neg_df = raw_data_df.loc[raw_data_df["target"]==4]
pos_df = raw_data_df.loc[raw_data_df["target"]==0]

# get first 5 records for both neg/pos
neg_df = neg_df.iloc[0:5].reset_index(drop=True)
pos_df = pos_df.iloc[0:5].reset_index(drop=True)
neg_df["clean_text"] = neg_df["text"]
pos_df["clean_text"] = pos_df["text"]

# clean new data
TAG_CLEANING_RE = "@\S+"
print("-----removing @tags-----")
# Remove @tags
neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))
pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))

# Smart lowercase
print("-----making lower case-----")
neg_df["clean_text"] = neg_df["clean_text"].str.lower()
pos_df["clean_text"] = pos_df["clean_text"].str.lower()

# Remove numbers
print("-----removing number-----")
def cleaning_numbers(data):
    return re.sub(r'\w*\d\w*', '', data)
neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: cleaning_numbers(x))
pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: cleaning_numbers(x))

# Remove links
print("-----removing links-----")
def cleaning_URLs(data):
    return re.sub('((www\S+)|(http\S+))', ' ', data)
neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: cleaning_URLs(x))
pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: cleaning_URLs(x))


print(neg_df)
print(pos_df)
# clean new data
# separate training data from test data
# create and test model
# check results