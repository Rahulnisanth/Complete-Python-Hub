
# SORTING THE WORDS & IGNORING THE SPACES :
def wordSort(words):
    return ' '. join(sorted(words.split(), key=str.casefold)) # Converting all the strings to lower and sorting them