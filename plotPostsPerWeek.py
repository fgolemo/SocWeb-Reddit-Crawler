import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn import linear_model, pipeline, preprocessing
import numpy as np
import cPickle as pickle

weeks = pickle.load(file('ppw.weeks.pickle'))
posts_per_week = pickle.load(file('ppw.posts_per_week.pickle'))
avg = pickle.load(file('ppw.avg.pickle'))
avg_weeks = pickle.load(file('ppw.avg_weeks.pickle'))


weeks_array = np.asarray(weeks)
ppw_array = np.asarray(posts_per_week)
polynomial_features = preprocessing.PolynomialFeatures(degree=2, include_bias=False)
linear_regression = linear_model.LassoLars()
pipeline = pipeline.Pipeline([("polynomial_features", polynomial_features), ("linear_regression", linear_regression)])
pipeline.fit(weeks_array[:,np.newaxis], ppw_array)
clf = linear_model.LassoLars()
clf.fit(weeks_array[:,np.newaxis], ppw_array)


plt.scatter(weeks, posts_per_week)
plt.scatter(weeks, pipeline.predict(weeks_array[:,np.newaxis]), color='red')
plt.scatter(avg_weeks, avg, color='green')
# plt.scatter(weeks, clf.predict(weeks_array[:,np.newaxis]), color='green')
plt.ylabel('posts per week')
plt.xlabel('weeks since joining')
plt.show()

