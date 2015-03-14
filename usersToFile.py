import cPickle as pickle
import os

users = list(pickle.load(file('users.pickle')))
pickle.dump(users, open("users.list.pickle.tmp", "wb"))
os.rename("users.list.pickle.tmp", "users.list.pickle")