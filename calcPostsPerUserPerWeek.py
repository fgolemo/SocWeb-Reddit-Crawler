import datetime
import os
import math

import cPickle as pickle

user_data = []

with open("submissions-0-8000.csv") as f:
    for line in f:
        user_data_line = []

        segments = line.split(",")
        join_date = datetime.datetime.fromtimestamp(int(segments[1]))
        user_data_line.append(int(segments[1]))

        posts = sorted(segments[3:])
        week_nrs = []

        for post in posts:
            post_date = datetime.datetime.fromtimestamp(int(post))
            date_diff = post_date - join_date
            week_nr = int(math.floor(date_diff.days / 7.0) + 1)
            week_nrs.append(week_nr)

        week_counts = dict((i, week_nrs.count(i)) for i in week_nrs)

        user_data_line.append(week_counts)
        user_data.append(user_data_line)

pickle.dump(user_data, open("ppw.userdata.pickle.tmp", "wb"))
os.rename("ppw.userdata.pickle.tmp", "ppw.userdata.pickle")

