import os
from requests import HTTPError
import praw
import cPickle as pickle
import sys

start = 0
limit = 10
userID = 0

if len(sys.argv) >= 2:
    userID = int(sys.argv[1])

if len(sys.argv) == 3:
    limit = int(sys.argv[2])

if len(sys.argv) == 4:
    start = int(sys.argv[2])
    limit = int(sys.argv[3])

logins = [{"username":"**********", "password":"**********"},
    {"username":"**********", "password":"**********"},
    {"username":"**********", "password":"**********"}
    ]

r = praw.Reddit('Research Project Crawler for User Behavior, VU Amsterdam, The Social Web 2015, bot {bot}/4 by u/fgolemo v 1.0.'.format(bot=userID))
r.login(username=logins[userID]['username'], password=logins[userID]['password'])

users = pickle.load(file('users.list.pickle'))

i = 0

userdata = []

for u in users[start:limit]:

    userdata_line = [u]
    try:
        redditor = r.get_redditor(u)
        userdata_line.append(str(redditor.created)[:-2])

        submissions = []
        submits = redditor.get_submitted(limit=10000)
        for submit in submits:
            submissions.append(str(submit.created)[:-2])

        comments = redditor.get_comments(limit=10000)
        for comment in comments:
            submissions.append(str(comment.created)[:-2])

        userdata_line.append(str(len(submissions)))
        userdata_line += submissions

        # userdata.append(userdata_line)
        print ",".join(userdata_line)

        i += 1
        if i >= limit:
            break

    except HTTPError:
        pass


# print userdata