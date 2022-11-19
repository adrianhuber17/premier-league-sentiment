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
from nltk.stem import WordNetLemmatizer
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
data = pd.read_csv('NLP/training_data_set.csv', encoding =DATASET_ENCODING , names=DATASET_COLUMNS)
print("---importing training data-----")
print(data.head())
print("-----changin target from 4 to 1 for positive comments")
X = data.iloc[:,[5]]
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
num_missing_desc = data.isnull().sum()[2]    # No. of values with msising descriptions
print('Number of missing values: ' + str(num_missing_desc))
data = data.dropna()

TAG_CLEANING_RE = "@\S+"
print("-----removing @tags-----")
# Remove @tags
X['text'] = X['text'].map(lambda x: re.sub(TAG_CLEANING_RE, ' ', x))

# Smart lowercase
print("-----making lower case-----")
X['text'] = X['text'].map(lambda x: x.lower())

# Remove numbers
print("-----removing number-----")
X['text'] = X['text'].map(lambda x: re.sub(r'\d+', ' ', x))

# Remove links
print("-----removing links-----")
TEXT_CLEANING_RE = "https?:\S+|http?:\S|[^A-Za-z0-9]+"
X['text'] = X['text'].map(lambda x: re.sub(TEXT_CLEANING_RE, ' ', x))

# Remove Punctuation
print("-----removing punctuation-----")
X['text']  = X['text'].map(lambda x: x.translate(x.maketrans('', '', string.punctuation)))

# Remove white spaces
print("-----removing white spaces-----")
X['text'] = X['text'].map(lambda x: x.strip())

# Tokenize into words
print("-----tokenizing into words-----")
X['text'] = X['text'].map(lambda x: word_tokenize(x))
 
# Remove non alphabetic tokens
print("-----removing non alphabetic tokens-----")
X['text'] = X['text'].map(lambda x: [word for word in x if word.isalpha()])

# Filter out stop words
print("-----filter out stop words-----")
stop_words = set(stopwords.words('english'))
X['text'] = X['text'].map(lambda x: [w for w in x if not w in stop_words])
    
# Word Lemmatization
print("-----Word lemmentization-----")
lem = WordNetLemmatizer()
X['text'] = X['text'].map(lambda x: [lem.lemmatize(word,"v") for word in x])

# Turn lists back to string
print("-----Turn tokenized list back to a string-----")
X['text'] = X['text'].map(lambda x: ' '.join(x))

print("-----Checking clean text column-----")
print(X.head())

#send clean data to csv
print("-----sending clean data and target to csv-----")
X.to_csv("NLP/clean_dataset.csv")
Y.to_csv("NLP/clean_target.csv")
