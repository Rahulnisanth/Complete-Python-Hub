# CREATING THE AUTOMATED SECURITY CODES :
# Note : download the diceware_pass_phrase_list in diceware.com on your cd
import secrets


def genre_pass(num_words, wordlist_path='diceware.wordlist.asc.txt'):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)
