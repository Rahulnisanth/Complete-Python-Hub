# FINDING THE NO.OF UNIQUE WORDS, RANK OF EACH WORD & TOTAL WORDS :
import re
import collections

def word_play(file_name):
    with open(file_name, 'r+', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-]+", file.read())
        all_words = [word.upper for word in all_words]
        print(f'TOTAL WORDS: {len(all_words)}')

        word_counts = collections.Counter(all_words)
        print('\nTOP WORDS:')
        for word in word_counts.most_common(10):
            print(f'{word[0]}\t{word[1]}')