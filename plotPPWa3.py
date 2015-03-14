import matplotlib.pyplot as plt
import cPickle as pickle
from scipy import stats

user_data = pickle.load(file('ppw.userdata.pickle'))

right_border = 1414058500
left_border = 1345889500

left_posts_per_month = []
right_posts_per_month = []

left = 0
right = 0

plt.figure(0)

for user in user_data:
    weeks = sorted(user[1])
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

    if int(user[0]) <= left_border:
        left += 1
        plt.plot(weeks, posts, color='blue')
        if len(user[1].values()) != 0:
            left_posts_per_month.append(sum(user[1].values())*1.0/len(user[1].values()))
        else:
            left_posts_per_month.append(0)
    if int(user[0]) >= right_border:
        right += 1
        plt.plot(weeks, posts, color='red')
        if len(user[1].values()) != 0:
            right_posts_per_month.append(sum(user[1].values())*1.0/len(user[1].values()))
        else:
            right_posts_per_month.append(0)

print left, right

print stats.ks_2samp(left_posts_per_month, right_posts_per_month)

plt.ylabel('posts per week')
plt.xlabel('weeks since joining')

plt.figure(1)
plt.hist(left_posts_per_month, bins=50)
plt.ylabel('avg posts per week')
plt.xlabel('number of users')

plt.figure(2)
plt.hist(right_posts_per_month, bins=50, color='red')
plt.ylabel('avg posts per week')
plt.xlabel('number of users')

plt.show()


