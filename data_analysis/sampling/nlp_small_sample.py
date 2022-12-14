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
import nltk
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
from nltk.corpus import stopwords

# import new data
columns = ["target","number","date","query","user","text"]
df = pd.read_csv("/Users/adrianhuber/football-sentiment/services/backend/app/NLP/train_model/training_data_set.csv",encoding_errors='ignore')
df.columns = columns
raw_data_df = df[["target","text"]]
print(raw_data_df)
# analyze new data
# clean new data
# separate training data from test data
# create and test model
# check results