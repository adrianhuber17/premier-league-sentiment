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

# time library :
import time

def clean_tweet_data(data):

    print("---importing  data-----")
    print(data.head())
    print(data.columns)

    # ----Display the column names of our dataset and additional information :-----
    print("-----data set additional information")
    column = data.columns[0]
    print("data shape: ",data.shape)
    print("column name: ", column)

    # ----Checking for Null values :----
    print("-----data set null values")
    print(np.sum(data.isnull().any(axis=1)))

    # Text-preprocessing
    print("-----text processing-----")
    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    TAG_CLEANING_RE = "@\S+"
    print("-----removing @tags-----")
    # Remove @tags
    data[column] = data[column].apply(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    # Smart lowercase
    print("-----making lower case-----")
    data[column] = data[column].str.lower()

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    # Remove numbers
    print("-----removing number-----")
    def cleaning_numbers(data):
        return re.sub('[0-9]+', '', data)
    data[column] = data[column].apply(lambda x: cleaning_numbers(x))

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    # Remove links
    print("-----removing links-----")
    def cleaning_URLs(data):
        return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)
    data[column] = data[column].apply(lambda x: cleaning_URLs(x))

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    # Remove Punctuation
    print("-----removing punctuation-----")
    english_punctuation_list = string.punctuation
    def cleaning_punctuations(text):
        translator = str.maketrans('', '', english_punctuation_list)
        return text.translate(translator)
    data[column] = data[column].apply(lambda x: cleaning_punctuations(x))

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    #Cleaning and removing repeating characters
    print("-----removing repeating characters-----")
    def cleaning_repeating_char(text):
        return re.sub(r'(.)1+', r'1', text)
    data[column] = data[column].apply(lambda x: cleaning_repeating_char(x))

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    # Filter out stop words
    print("-----filter out stop words-----")
    stop_words = set(stopwords.words('english'))
    def cleaning_stopwords(text):
        return " ".join([word for word in str(text).split() if word not in stop_words])
    data[column] = data[column].apply(lambda text: cleaning_stopwords(text))

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    # Remove white spaces
    print("-----removing white spaces-----")
    data[column] = data[column].apply(lambda x: x.strip())

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))

    # Tokenize into words
    print("-----tokenizing into words-----")
    data[column] = data[column].apply(word_tokenize)

    # Applying Stemming
    print("-----Applying Stemming-----")
    st = PorterStemmer()
    def stemming_on_text(data):
        text = [st.stem(word) for word in data]
        return data
    data[column] = data[column].apply(lambda x: stemming_on_text(x))

    # ----Applying Lemmatizer :----
    print("-----Applying Lemmatizer-----")
    lm = WordNetLemmatizer()
    def lemmatizer_on_text(data):
        text = [lm.lemmatize(word) for word in data]
        return data
    data[column] = data[column].apply(lambda x: lemmatizer_on_text(x))
    
    # Turn lists back to string
    print("-----Turn tokenized list back to a string-----")
    data[column] = data[column].apply(lambda x: ' '.join(x))

    # Missing Values
    check_nan = data[column].isnull().values.any()
    print('missing values?: ' + str(check_nan))
    print(data.head())

    #send clean data to csv
    print("-----data is clean-----")
    # data.to_csv("NLP/process_tweets/clean_team_tweets.csv",na_rep='NULL')
    return data