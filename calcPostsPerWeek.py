import datetime
import os
import math

import cPickle as pickle

weeks = []
posts_per_week = []
ppw_dict = {}

with open("submissions-0-8000.csv") as f:
    for line in f:
        segments = line.split(",")
        join_date = datetime.datetime.fromtimestamp(int(segments[1]))
        # print join_date
        posts = sorted(segments[3:])
        week_nrs = []

        for post in posts:
            post_date = datetime.datetime.fromtimestamp(int(post))
            date_diff = post_date - join_date
            week_nr = int(math.floor(date_diff.days / 7.0) + 1)
            week_nrs.append(week_nr)

        week_counts = dict((i, week_nrs.count(i)) for i in week_nrs)

        for week, count in week_counts.iteritems():
            if week in ppw_dict:
                ppw_dict[week].append(count)
            else:
                ppw_dict[week] = [count]

        weeks += week_counts.keys()
        posts_per_week += week_counts.values()

ppw_weeks = ppw_dict.keys()
ppw_avg = [sum(cs)*1.0/len(cs) for w,cs in ppw_dict.iteritems()]

pickle.dump(weeks, open("ppw.weeks.pickle.tmp", "wb"))
pickle.dump(posts_per_week, open("ppw.posts_per_week.pickle.tmp", "wb"))
pickle.dump(ppw_weeks, open("ppw.avg_weeks.pickle.tmp", "wb"))
pickle.dump(ppw_avg, open("ppw.avg.pickle.tmp", "wb"))
os.rename("ppw.weeks.pickle.tmp", "ppw.weeks.pickle")
os.rename("ppw.posts_per_week.pickle.tmp", "ppw.posts_per_week.pickle")
os.rename("ppw.avg_weeks.pickle.tmp", "ppw.avg_weeks.pickle")
os.rename("ppw.avg.pickle.tmp", "ppw.avg.pickle")

