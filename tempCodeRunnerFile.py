# SERIALIZING & DE-SERIALIZING A DICT FILE :
import pickle

def save_file(content, file_name):
    with open(file_name, mode="wb") as file:
        pickle.dump(content, file)
    
def load_file(file_name):
    with open(file_name, mode="rb") as file:
        return pickle.load(file)


my_dict = {1:'a', 2:'z', 3:'g'}
save_file(my_dict, '../pytuts_ser.txt')
load_file('../pytuts_ser.txt')