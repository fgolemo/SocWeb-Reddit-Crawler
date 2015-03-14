import os
from requests import HTTPError
import praw
import cPickle as pickle
import sys
import timeit

timer_start = timeit.default_timer()

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

logins = [{"client_id":"**********", "client_secret":"********************"},
    {"client_id":"**********", "client_secret":"********************"},
    {"client_id":"**********", "client_secret":"********************"},
    {"client_id":"**********", "client_secret":"********************"}
    ]
access_info = [{'access_token': u'******************************', 'scope': set([u'identity']), 'refresh_token': u'******************************'},
    {'access_token': u'******************************', 'scope': set([u'identity']), 'refresh_token': u'******************************'},
    {'access_token': u'******************************', 'scope': set([u'identity']), 'refresh_token': u'******************************'},
    {'access_token': u'******************************', 'scope': set([u'identity']), 'refresh_token': u'******************************'}]

r = praw.Reddit('Research Project Crawler for User Behavior, VU Amsterdam, The Social Web 2015, bot {bot}/2 by u/fgolemo v 1.0.'.format(bot=userID+1))
r.set_oauth_app_info(client_id=logins[userID]['client_id'],
                     client_secret=logins[userID]['client_secret'],
                     redirect_uri='http://127.0.0.1:65010/authorize_callback')
r.set_access_credentials(**access_info[userID])

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

        timer_now = timeit.default_timer()
        if (timer_now - timer_start)/60/30 >= 1:
            access_info[userID] = r.refresh_access_information(access_info[userID]['refresh_token'])
            r.set_access_credentials(**access_info[userID])
            timer_start = timer_now
    except HTTPError:
        pass


# print userdata
