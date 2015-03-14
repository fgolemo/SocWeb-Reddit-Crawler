import os
import praw
import cPickle as pickle

N = 30
limit = 1000

r = praw.Reddit('top N subreddits name crawler by u/fgolemo v 1.0.')
r.login(username="**********", password="**********")

seen = set()
submissions = r.get_content(url="http://www.reddit.com/top.json", limit=limit)

i = 0
for sub in submissions:
    # seen.add((sub.subreddit.fullname, sub.subreddit.display_name))
    seen.add(sub.subreddit.display_name)
    i += 1
    if i % 10 == 0:
        print "parsed {current}/{total} submissions".format(current=i, total=limit)
    if len(seen) == N:
        break

pickle.dump(seen, open("subreddits.pickle.tmp", "wb"))
os.rename("subreddits.pickle.tmp", "subreddits.pickle")

print "number of subreddits found: ", len(seen)

for s in seen:
    print s


