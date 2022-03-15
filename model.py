from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math
import main as mn

# figure out x, y data
y = mn.data["charges"]
X = mn.data.drop("charges", axis = 1)
lin_reg = LinearRegression() # the method of prediction

# train data and test
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.80, random_state=1)
lin_reg.fit(train_X, train_y)

print("Linear regression result >", lin_reg.score(test_X, test_y).round(3))

# predict value of y
y_predict = lin_reg.predict(test_X)
# print(y_predict)
sqr = math.sqrt(mean_squared_error(test_y, y_predict))
print(sqr)
data_new = train_X[:1]
print(data_new)
estimate = lin_reg.predict(data_new)

# compare predicting data and original data
print('machine prediction > ', estimate[0])
print('real value > ', train_y[:1])


