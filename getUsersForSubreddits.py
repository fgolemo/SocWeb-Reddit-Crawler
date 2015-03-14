import os
import praw
import cPickle as pickle

limit = 1000

r = praw.Reddit('username crawler from hot subreddits by u/fgolemo v 1.0.')
r.login(username="**********", password="**********")

subreddits = pickle.load(file('subreddits.pickle'))

users = set()

for subreddit in subreddits:
    topics = r.get_content(url='http://www.reddit.com/r/{subreddit}/hot.json'.format(subreddit=subreddit), params={"sort": "top", "t": "all"}, limit=limit)
    for topic in topics:
        if topic.author is not None:
            users.add(topic.author.name)
    print "subreddit '{subreddit}' done, total user count: {users}".format(subreddit=subreddit, users=len(users))

pickle.dump(users, open("users.pickle.tmp", "wb"))
os.rename("users.pickle.tmp", "users.pickle")

print "number of users found: ", len(users)

# for u in users:
#     print u
