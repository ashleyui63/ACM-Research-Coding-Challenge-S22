import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_absolute_error, mean_squared_error
#%matplotlib inline

#puts csv file into dataframe
mrdata = pd.read_csv("mushrooms.csv")
mrdata.shape
#mrdata.head()


#splits dataframe into labels
X = mrdata.drop('class', axis=1)
X = OneHotEncoder().fit_transform(X)
y = mrdata['class']
#y = OneHotEncoder().fit_transform(y) THIS NOT NEED. YOU DON'T ENCODE YOUR TARGET VARIABLE

# splits labels into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state=2)


# svcclassifer = SVC(kernel='l') FAILED ATTEMPT AT SVM CLASSIFER
# svcclassifer.fit(X_train, y_train)

# y_pred = svcclassifier.predict(X_test)
LR = LogisticRegression()
LR = LR.fit(X_train,y_train)

predictions = LR.predict(X_test)
score = accuracy_score(y_test, predictions)







