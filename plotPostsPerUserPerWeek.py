import matplotlib.pyplot as plt
import cPickle as pickle

user_data = pickle.load(file('ppw.userdata.pickle'))

for user in user_data:
    weeks = user[1].keys()
    posts = user[1].values()
    plt.plot(weeks, posts)

plt.ylabel('posts per week')
plt.xlabel('weeks since joining')
plt.show()

