# sklearn :
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

# plotting :
import seaborn as sns
import matplotlib.pyplot as plt

#utilities:
import pandas as pd
import numpy as np
import time

# -----importing clean training data-----
print("-----importing clean training data-----")
DATASET_ENCODING = "ISO-8859-1"
DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
data = pd.read_csv('services/NLP/train_model/clean_dataset.csv',encoding=DATASET_ENCODING,names=DATASET_COLUMNS,low_memory=False)
# y_data = pd.read_csv('NLP/clean_target.csv',encoding=DATASET_ENCODING)
print("-----Traning dataset null values-----")
check_nan = data['text'].isnull().values.any()
print("missing values total: ",np.sum(data.isnull().any(axis=1)))
print('missing values?: ' + str(check_nan))
data = data.dropna()
check_nan = data['text'].isnull().values.any()

print("-----Remove dataset null values-----")
print('missing values?: ' + str(check_nan))
print("missing values total: ",np.sum(data.isnull().any(axis=1)))

# ----Separating input feature and label :----
print("-----creating training and test data-----")
X = data['text']
y = data['target']


# -----Separating the 95% data for training data and 5% for testing data-----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=26105111)
print("TRAIN size:", len(X_train))
print("TEST size:", len(X_test))

# -----Fit the TF-IDF Vectorizer----- 
print("-----Fit the TF-IDF Vectorizer-----")
vectoriser = TfidfVectorizer(ngram_range=(1,2), max_features=500000)
vectoriser.fit(X_train)
print('No. of feature_words: ', len(vectoriser.get_feature_names()))

# -----Transform the data using TF-IDF Vectorizer-----
print("-----Transform the data using TF-IDF Vectorizer-----")
X_train = vectoriser.transform(X_train)
X_test  = vectoriser.transform(X_test)

def model_evaluate(model):
    # Predict values for Test dataset
    y_pred = model.predict(X_test)
    #model test score
    print("-----model test score-----")
    # Print the evaluation metrics for the dataset.
    print(classification_report(y_test, y_pred))
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    categories = ['Negative','Positive']
    group_names = ['True Neg','False Pos', 'False Neg','True Pos']
    group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]
    labels = [f'{v1}n{v2}' for v1, v2 in zip(group_names,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    sns.heatmap(cf_matrix, annot = labels, cmap = 'Blues',fmt = '',
    xticklabels = categories, yticklabels = categories)
    plt.xlabel("Predicted values", fontdict = {'size':14}, labelpad = 10)
    plt.ylabel("Actual values" , fontdict = {'size':14}, labelpad = 10)
    plt.title ("Confusion Matrix", fontdict = {'size':18}, pad = 20)
    plt.show()

# Model-1 : Bernoulli Naive Bayes.
print("-----creating and training Bernoulli Naive Bayes Model-----")
BNBmodel = BernoulliNB()
start = time.time()
BNBmodel.fit(X_train, y_train)
end = time.time()
print("The execution time of this model is {:.2f} seconds\n".format(end-start))
print("-----evaluating model-----")
model_evaluate(BNBmodel)
y_pred1 = BNBmodel.predict(X_test)
print('test_predictions: ',y_pred1)
print("model score: ",BNBmodel.score(X_test,y_test))


#saving model
print("-----saving model-----")
import pickle
file_name = 'services/NLP/final_model/bernoulli_model.sav'
pickle.dump(BNBmodel,open(file_name,'wb'))
print("-----saving vectorizer-----")
file_name_vectorizer = "services/NLP/final_model/vectorizer.sav"
pickle.dump(vectoriser,open(file_name_vectorizer,'wb'))