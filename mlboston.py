#prevent unnecessary warnings
from cProfile import label
from operator import mod
from tkinter.font import names
import warnings
from pyparsing import alphas

warnings.filterwarnings("ignore")

#basic packages of data science
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import seaborn as sns

#set attributes to prevent garbled characters in chinese
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus']=False

#introduce machine learning, preprocessing, model selection and evaluation indicators
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

#import the Boston dataset
from sklearn.datasets import load_boston
#introduce algorithms
from sklearn.linear_model import RidgeCV, LassoCV, LinearRegression, ElasticNet
#compared with SVC, it is the reression form of SVM
from sklearn.svm import SVR
#integrate algorithms
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

#load the boston house price data
boston= load_boston()
#x features and y labels
x=boston.data
y=boston.target

#display related attributes 
print('Feature column name')
print(boston.feature_names)
print("Sample data volume: %d, number of features: %d"% x.shape)
print("Target sample data volume: %d"% y.shape[0])

"""
#feature column name
x=pd.DataFrame(boston.data, columns=boston.feature_names)
print(x.head())
#visualize label distribution and output the graph******
sns.distplot(tuple(y), kde=False, fit=st.norm)
plt.show()
"""
#segment the data
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=28)

#standardize the dataset
ss=StandardScaler()
x_train=ss.fit_transform(x_train)
x_test=ss.transform(x_test)
print(x_train[0:100])

#set the model name
names=['LinearRegression', 'Ridge', 'Lasso', 'Random Forest', 'GBDT', 'Support Vector Regression', 'ElasticNet', 'XgBoost']

# define the model
#cv is Cross Validation
models=[LinearRegression(),
        RidgeCV(alphas=(0.001, 0.1, 1), cv=3),
        LassoCV(alphas=(0.001, 0.1, 1), cv=5),
        RandomForestRegressor(n_estimators=10),
        GradientBoostingRegressor(n_estimators=30),
        SVR(),
        ElasticNet(alpha=0.001, max_iter=1000),
        XGBRegressor()
        ]

#output the R2 score of all regression models
#define the R2 scoring function
def R2(model, x_train, x_test, y_train, y_test):
        model_fitted=model.fit(x_train,y_train)
        y_pred=model_fitted.predict(x_test)
        score=r2_score(y_test, y_pred)
        return score

#traverse all models to score
for name, model in zip(names, models):
        score=R2(model, x_train, x_test, y_train, y_test)
        print("{}: {:.6f}, {:.4f}".format(name,score.mean(),score.std()))


#****
#build the model
'''     
'kernel': kernel function 
'C': SVR regularization factor 'gamma': 
'rbf', 'poly' and 'sigmoid' kernel function coefficient, which affects the model performance 

'''
parameters={
        'kernel':['linear', 'rbf'],
        'C':[0.1, 0.5, 0.9, 1, 5],
        'gamma':[0.001, 0.01, 0.1, 1]
}
model=GridSearchCV(SVR(), param_grid=parameters, cv=3)
print(model.fit(x_train, y_train))

print("Optimal parameter list:", model.best_params_)
print("Optimal model:", model.best_estimator_)
print("Optimal R2 value:", model.best_score_)
#**********

#perform visualization
ln_x_test=range(len(x_test))
y_predict=model.predict(x_test)

plt.figure(figsize=(16,8), facecolor='w')
plt.plot(ln_x_test, y_test, 'r-', lw=2, label=u'Value')
plt.plot(ln_x_test, y_predict, 'g-', lw=3, label=u'Estimated value of the SVR algorithm, $R^2$=%.3f' %
(model.best_score_))



