# COLLECTING THE MEDALS OF PLAYER OF OLYMPICS :
from collections import namedtuple

with open('olympics.txt', 'r', encoding='utf-8') as file:
    olympics = file.read()

medal = namedtuple('medal', ['city', 'edition', 'sport', 'discipline', 'athlete', 'event', 'event_gender', 'medal' ])

medals = [medal(* line.split(';')) for line in olympics.splitlines()[1:]]

def get_medals(**kwargs):
    '''Return a list of medal namedtuples'''
    return [
            medal 
            for medal in medals 
            if all(getattr(medal, key) == value 
            for key, value in kwargs.items())
            ]