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

# -----Importing the dataset :-----
DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
DATASET_ENCODING = "ISO-8859-1"
data = pd.read_csv('services/NLP/train_model/training_data_set.csv', encoding =DATASET_ENCODING , names=DATASET_COLUMNS)
print("---importing training data-----")
print(data.head())
print("-----changin target from 4 to 1 for positive comments")
# X = data.iloc[:,[5]]
Y = data.iloc[:,0]
Y[Y == 4] = 1
print(data.head())


# ----Display the column names of our dataset and additional information :-----
print("-----Traning data set additional information")
print(data.columns)
print(data.shape)
print(data.info)
print(data.dtypes)

# ----Checking for Null values :----
print("-----Traning data set null values")
print(np.sum(data.isnull().any(axis=1)))

# ----Rows and columns in the dataset :-----
print("-----Traning data set rows and columns-----")
print('Count of columns in the data is:  ', len(data.columns))
print('Count of rows in the data is:  ', len(data))

# -----Checking unique Target Values :-----
print("-----Training data set unique values")
print('unique target values: ',data['target'].unique())
print('number of unique target values: ', data['target'].nunique())
print(data.groupby('target').count())


# # -----Plotting the distribution for dataset :-----
# print("-----distribution of training data set-----")
# ax = data.groupby('target').count().plot(kind='bar', title='Distribution of data',legend=False)
# # Naming 0 -> Negative , and 4 -> Positive
# ax.set_xticklabels(['Negative','Positive'], rotation=0)
# # Storing data in lists :
# text, sentiment = list(data['text']), list(data['target'])
# plt.show()


# Text-preprocessing
print("-----text processing-----")
# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

TAG_CLEANING_RE = "@\S+"
print("-----removing @tags-----")
# Remove @tags
data['text'] = data['text'].apply(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

# Smart lowercase
print("-----making lower case-----")
data['text'] = data['text'].str.lower()

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

# Remove numbers
print("-----removing number-----")
def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)
data['text'] = data['text'].apply(lambda x: cleaning_numbers(x))

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

# Remove links
print("-----removing links-----")
def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)
data['text'] = data['text'].apply(lambda x: cleaning_URLs(x))

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

# Remove Punctuation
print("-----removing punctuation-----")
english_punctuation_list = string.punctuation
def cleaning_punctuations(text):
    translator = str.maketrans('', '', english_punctuation_list)
    return text.translate(translator)
data['text'] = data['text'].apply(lambda x: cleaning_punctuations(x))

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

#Cleaning and removing repeating characters
print("-----removing repeating characters-----")
def cleaning_repeating_char(text):
    return re.sub(r'(.)1+', r'1', text)
data['text'] = data['text'].apply(lambda x: cleaning_repeating_char(x))

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

# Filter out stop words
print("-----filter out stop words-----")
stop_words = set(stopwords.words('english'))
def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])
data['text'] = data['text'].apply(lambda text: cleaning_stopwords(text))

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

# Remove white spaces
print("-----removing white spaces-----")
data['text'] = data['text'].apply(lambda x: x.strip())

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

# Tokenize into words
print("-----tokenizing into words-----")
data['text'] = data['text'].apply(word_tokenize)

# Applying Stemming
print("-----Applying Stemming-----")
st = PorterStemmer()
def stemming_on_text(data):
    text = [st.stem(word) for word in data]
    return data
data['text'] = data['text'].apply(lambda x: stemming_on_text(x))

# ----Applying Lemmatizer :----
print("-----Applying Lemmatizer-----")
lm = WordNetLemmatizer()
def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data
data['text'] = data['text'].apply(lambda x: lemmatizer_on_text(x))
 
# Turn lists back to string
print("-----Turn tokenized list back to a string-----")
data['text'] = data['text'].apply(lambda x: ' '.join(x))

# Missing Values
check_nan = data['text'].isnull().values.any()
print('missing values?: ' + str(check_nan))

print("-----Checking data-----")
data = data.dropna()
print(data.head())
#send clean data to csv
print("-----sending clean data to csv-----")
data.to_csv("services/NLP/train_model/clean_dataset.csv",na_rep='NULL')
