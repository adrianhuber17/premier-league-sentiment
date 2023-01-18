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

def import_data():

    ##### import new data #####
    print("DATA IMPORT")
    columns = ["target","number","date","query","user","text"]
    df = pd.read_csv("/Users/adrianhuber/football-sentiment/services/backend/app/NLP/train_model/training_data_set.csv",encoding_errors='ignore')
    df.columns = columns

    # filtered data for text and target
    raw_data_df = df[["target","text"]]

    return raw_data_df

class NLP:

    def clean_data(self,raw_data_df):
        """inputs an unorganized raw dataframe and outputs a csv with clean data"""
        raw_data_df = raw_data_df.assign(clean_text=raw_data_df['text'])
        # raw_data_df["clean_text"] = raw_data_df["text"]

        ##### clean new data #####
        TAG_CLEANING_RE = "@\S+"
        print("-----removing @tags-----")
        # Remove @tags
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))

        # Smart lowercase
        print("-----making lower case-----")
        # neg_df["clean_text"] = neg_df["clean_text"].str.lower()
        # pos_df["clean_text"] = pos_df["clean_text"].str.lower()
        raw_data_df["clean_text"] = raw_data_df["clean_text"].str.lower()


        # Remove numbers
        print("-----removing number-----")
        def cleaning_numbers(data):
            return re.sub(r'\w*\d\w*', '', data)
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: cleaning_numbers(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: cleaning_numbers(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: cleaning_numbers(x))


        # Remove links
        print("-----removing links-----")
        def cleaning_URLs(data):
            return re.sub('((www\S+)|(http\S+))', ' ', data)
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: cleaning_URLs(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: cleaning_URLs(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: cleaning_URLs(x))

        # Remove domains
        print("-----removing domains-----")
        def cleaning_URLs(data):
            return re.sub(r"[^\s]*\.(com|org|net)\S*", ' ', data)
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: cleaning_URLs(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: cleaning_URLs(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: cleaning_URLs(x))

        #removing punctuations
        print("-----removing punctuation-----")
        english_punctuation_list = string.punctuation
        def cleaning_punctuations(text):
            translator = str.maketrans('', '', english_punctuation_list)
            return text.translate(translator)
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: cleaning_punctuations(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: cleaning_punctuations(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: cleaning_punctuations(x))

        # Filter out stop words
        print("-----filter out stop words-----")
        stop_words = set(stopwords.words('english'))
        def cleaning_stopwords(text):
            return " ".join([word for word in str(text).split() if word not in stop_words])
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda text: cleaning_stopwords(text))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda text: cleaning_stopwords(text))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda text: cleaning_stopwords(text))

        # Remove emojis
        print("-----removing emojis-----")
        def remove_emojis_and_text(text):
            emoji_pattern = re.compile("([\U0001f600-\U0001f64f\U0001f300-\U0001f5ff\U0001f680-\U0001f6ff\U0001f1e0-\U0001f1ff]+\S*)", flags=re.UNICODE)
            return emoji_pattern.sub(r'', text)

        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda text: remove_emojis_and_text(text))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda text: remove_emojis_and_text(text))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda text: remove_emojis_and_text(text))

        # Remove white spaces
        print("-----removing white spaces-----")
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: x.strip())
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: x.strip())
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: x.strip())

        # Tokenize into words
        print("-----tokenizing into words-----")
        # neg_df["clean_text"] = neg_df["clean_text"].apply(word_tokenize)
        # pos_df["clean_text"] = pos_df["clean_text"].apply(word_tokenize)
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(word_tokenize)

        # Removing words with one letter
        print("-----removing words with one letter-----")
        def remove_words_len_one(sentence):
            return [word for word in sentence if len(word) > 1 or not word.isalpha()]

        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: remove_words_len_one(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: remove_words_len_one(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: remove_words_len_one(x))

        # Applying Stemming
        print("-----Applying Stemming-----")
        st = PorterStemmer()
        def stemming_on_text(data):
            text = [st.stem(word) for word in data]
            return text
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: stemming_on_text(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: stemming_on_text(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: stemming_on_text(x))

        # ----Applying Lemmatizer :----
        print("-----Applying Lemmatizer-----")
        lm = WordNetLemmatizer()
        def lemmatizer_on_text(data):
            text = [lm.lemmatize(word) for word in data]
            return text
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: lemmatizer_on_text(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: lemmatizer_on_text(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: lemmatizer_on_text(x))

        # Turn lists back to string
        print("-----Turn tokenized list back to a string-----")
        # neg_df["clean_text"] = neg_df["clean_text"].apply(lambda x: ' '.join(x))
        # pos_df["clean_text"] = pos_df["clean_text"].apply(lambda x: ' '.join(x))
        raw_data_df["clean_text"] = raw_data_df["clean_text"].apply(lambda x: ' '.join(x))

        # check_nan_neg = neg_df["clean_text"].isnull().values.any()
        # check_nan_pos = pos_df["clean_text"].isnull().values.any()
        # print('missing values negative?: ' + str(check_nan_neg))
        # print('missing values positive?: ' + str(check_nan_pos))

        check_nan_pos = raw_data_df["clean_text"].isnull().values.any()
        print('missing values?: ' + str(check_nan_pos))


        # print(neg_df)
        # print(pos_df)
        print(raw_data_df)
        raw_data_df.to_csv("/Users/adrianhuber/football-sentiment/data_analysis/sampling/clean_training_data.csv")

    def train_model(self):
        """trains model with clean data and outputs a working model"""
        # separate training data from test data
        # create and test model
        # check results
        pass

if __name__ == "__main__":

    raw_data_df = import_data()
    nlp = NLP()
    nlp.clean_data(raw_data_df=raw_data_df)
    nlp.train_model()
    