# CALCULATING THE AVERAGE RACETIME OF ATHLETES :
import datetime
import re

def get_rhine_times():
    races = input()
    rhine = []
    def get_time(line):
        return re.findall(r'\d{2}:\S+', line)[0]
    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
            rhine.append(get_time(line))
    return rhine

def get_average():
    racetimes = get_rhine_times()
    total = datetime.timedelta()
    for racetime in racetimes:
        try:
            min, sec, ms = re.split(r'[:.]+', racetime)
            total += datetime.timedelta(minutes=int(min), seconds=int(sec), milliseconds=int(ms))
        except ValueError:
            min, sec = re.split(r'[:.]+', racetime)
            total += datetime.timedelta(minutes=int(min), seconds=int(sec))
    return f'{total / len(racetimes)}'[2:-5]