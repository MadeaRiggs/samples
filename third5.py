from numpy import pi
from sklearn import linear_model

X=[[0,0], [1,1], [2,2]]
y=[0,1,2]
reg=linear_model.LinearRegression()
reg.fit(X, y)
print(reg.coef_)

#transformers and preprocessors
from sklearn.preprocessing import StandardScaler
X=[[0,0], [1,1], [2,2]]
print(StandardScaler().fit(X).transform(X))

from sklearn.preprocessing import MinMaxScaler
data=MinMaxScaler(feature_range=(0., 1.)).fit_transform(X)
print(data)

"""
A pipeline offers the same API as a regualr estimator.It can be fitted and used for prediction with fit and predict. It prevents data leakage
"""
from sklearn.pipeline import make_pipeline

#create a pipeline object
pipe=make_pipeline(
    StandardScaler(),
    linear_model.LinearRegression()
)
pipe.fit(X, y) #fit the whole pipeline
print(pipe[1].coef_) #coefficient

#model evaluation since fitting a model to some data does not entail that it will predict well on unseen data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

x_train, x_test, y_train, y_test=train_test_split(X, y, test_size=0.1)
pipe.fit(x_train, y_train)
print(mean_squared_error(y_test, pipe.predict(x_test)))

