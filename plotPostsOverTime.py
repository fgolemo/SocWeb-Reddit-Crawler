import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn import linear_model, pipeline, preprocessing
import numpy as np

dates = []
dates_ts = []
posts = []

min_date = 9999999999
max_date = 0000000000


with open("submissions-0-8000.csv") as f:
    for line in f:
        segments = line.split(",")

        dates_ts.append(int(segments[1]))
        date = datetime.datetime.fromtimestamp(int(segments[1]))
        dates.append(date)
        posts.append(int(segments[2]))

        if (int(segments[1]) > max_date):
            max_date = int(segments[1])
        if (int(segments[1]) < min_date):
            min_date = int(segments[1])

date_avg = sum(dates_ts)*1.0/len(dates_ts)
print date_avg

years = mdates.YearLocator()  # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

# load a numpy record array from yahoo csv data with fields date,
# open, close, volume, adj_close from the mpl-data/example directory.
# The record array stores python datetime.date as an object array in
# the date column

fig, ax = plt.subplots()

dates_array = np.asarray(dates_ts)
posts_array = np.asarray(posts)
# clf = linear_model.LassoLars()
# clf.fit(dates_array[:,np.newaxis], posts_array)
polynomial_features = preprocessing.PolynomialFeatures(degree=2, include_bias=False)
linear_regression = linear_model.LassoLars()
pipeline = pipeline.Pipeline([("polynomial_features", polynomial_features), ("linear_regression", linear_regression)])
pipeline.fit(dates_array[:,np.newaxis], posts_array)


ax.scatter(dates, posts)
ax.scatter(dates, pipeline.predict(dates_array[:,np.newaxis]), color='red')


# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

datemin = datetime.date(datetime.datetime.fromtimestamp(min_date).year, 1, 1)
datemax = datetime.date(datetime.datetime.fromtimestamp(max_date).year + 1, 1, 1)
ax.set_xlim(datemin, datemax)


ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
# ax.format_ydata = price
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

plt.ylabel('total number of posts per user')
plt.xlabel('join date')

plt.show()
