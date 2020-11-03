import pickle


def create_data_file(list_score):
    with open('donnees', 'wb') as data_file:
        mon_pickler = pickle.Pickler(data_file)
        mon_pickler.dump(list_score)
