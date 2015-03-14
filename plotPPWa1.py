import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn import linear_model, pipeline, preprocessing
import numpy as np
import cPickle as pickle

user_data = pickle.load(file('ppw.userdata.pickle'))


i = 0
for user in user_data:
    weeks = sorted(user[1])
    skip = True
    prev_week = 0
    for week in weeks:
        if week - prev_week >= 52:
            skip = False
            break
        prev_week = week
    if skip:
        continue

    posts = [value for (key, value) in sorted(user[1].items())]

    skip = False
    # remove outlier(s):
    for post in posts:
        if post > 1600:
            print 'skipping'
            skip = True
            break
    if skip:
        continue


    plt.plot(weeks, posts)
    i += 1

print i

plt.ylabel('posts per week')
plt.xlabel('weeks since joining')
plt.show()

