# -*- coding: utf-8 -*-
"""winequalityanalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cYTtPkhs-XmDIF_sITFKfOxry_eLtlYi

# New Section
"""

import numpy as np
import pandas.util.testing as tm
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px
import io

"""# New Section"""

from google.colab import files
uploaded = files.upload()

#reading data 
df2 = pd.read_csv(io.BytesIO(uploaded['UCI MACHINE LEARNING REPOSITORY.csv']))

print("rows,columns:"+str(df2.shape))
print(df2)

print("rows,columns:"+str(df2.shape))

#finding missing values
print(df2.isna().sum())

fig=px.histogram(df2,x='quality')
fig.show()

#grouping the dataset 
conditions=[
            (df2['quality']>=7),
            (df2['quality']<=4)
]
rating=['best','bad']
# Create Classification version of target variable
df2['rating'] = np.select(conditions, rating, default='good')
df2.rating.value_counts()

df2.groupby('rating').mean()

corr = df2.corr()
plt.pyplot.subplots(figsize=(15,10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, 
            annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

corr['quality'].sort_values(ascending=False)

sns.boxplot(x='rating',y='alcohol',data=df2)

sns.boxplot(x='rating',y='sulphates',data=df2)

sns.boxplot(x='rating',y='citric acid',data=df2)

sns.boxplot(x='rating',y='fixed acidity',data=df2)

sns.boxplot(x='rating',y='pH',data=df2)

# Separate feature variables and target variable
X = df2.drop(['quality','rating'], axis = 1)
y = df2['rating']
X

y

# Normalize feature variables
from sklearn.preprocessing import StandardScaler
X_features = X
X = StandardScaler().fit_transform(X)

# Splitting the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)

len(X_train)

#DECISION TREE MODEL
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
model1 = DecisionTreeClassifier(random_state=1)
model1.fit(X_train, y_train)

#testing using decision tree model
y_pred1 = model1.predict(X_test)
print(classification_report(y_test, y_pred1))

print("Accurcy using Decision tree is ",model1.score(X_test,y_test))

#RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier
model2 = RandomForestClassifier(random_state=1)
model2.fit(X_train, y_train)

#testing using Random Forest model
y_pred2 = model2.predict(X_test)
print(classification_report(y_test, y_pred2))

print("Accuracy using Random forest is ",model2.score(X_test,y_test))

#SVM model
from sklearn import svm
model3= svm.SVC()
model3.fit(X_train, y_train)

#testing
y_pred3=model3.predict(X_test)
print(classification_report(y_test,y_pred3))

print('accuracy using SVM is ',model3.score(X_test,y_test))

def write_results(result):
    f = open('results.txt', 'a', encoding='utf-8', newline='\n')
    wr = csv.writer(f, lineterminator = '\n')
    for i in range(len(result)):
        line = [int(result[i,0]),"1:"+str(result[i,1]),"2:"+str(result[i,2]),"3:"+str(result[i,3]),"4:"+str(result[i,4]),"5:"+str(result[i,5]),"6:"+str(result[i,6]),"7:"+str(result[i,7]),"8:"+str(result[i,8])]
#         print(line)
        wr.writerow(line)
    f.close()

x=[[7.4 , 0.7 , 0, 1.9 , 0.076 , 11 , 34 , 0.9978 , 3.51 , 0.56 , 9.4]]

y_pred = model2.predict(x)
print(y_pred)