import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn import linear_model, pipeline, preprocessing
import numpy as np
import cPickle as pickle

user_data = pickle.load(file('ppw.userdata.pickle'))

postings_per_month_total = []

j = 0
for user in user_data:

    weeks = sorted(user[1])
    # posts = [value for (key, value) in sorted(user[1].items())]
    if len(weeks) == 0:
        print user
        continue

    highest_week = max(weeks)
    month_posts = []
    month_buffer = []
    week_count = 0
    for i in range(1, highest_week):
        if i in user[1]:
            month_buffer.append(user[1][i])
        else:
            month_buffer.append(0)

        week_count += 1
        if week_count == 4:
            week_count = 0
            month_posts.append(sum(month_buffer))
            month_buffer = []

    if len(month_buffer) > 0:
        month_posts.append(sum(month_buffer))

    if len(month_posts) > 0:
        postings_per_month = sum(month_posts)/len(month_posts)
        postings_per_month_total.append(postings_per_month)
        j += 1

print j

print postings_per_month_total[643:700]

plt.hist(postings_per_month_total, bins=50)
plt.ylabel('number of users')
plt.xlabel('avg postings per month')
plt.show()

