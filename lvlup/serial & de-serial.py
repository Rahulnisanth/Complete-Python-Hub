# SERIALIZING & DE-SERIALIZING A DICT FILE :
import pickle

def save_file(content, file_name): # Saving the contents in a file using pickle.dump()
    with open(file_name, mode="wb") as file:
        pickle.dump(content, file)
    
def load_file(file_name): # Encrypting the contents in the file using pickle.load()
    with open(file_name, mode="rb") as file:
        return pickle.load(file)