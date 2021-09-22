import pickle

msg = 'I hate web'

with open('data.pickle', 'wb') as f:
    pickle.dump(msg, f)