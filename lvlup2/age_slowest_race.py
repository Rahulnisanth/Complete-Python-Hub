from datetime import date
import datetime
import re


def get_event_time(line):
    def get_date(date_):
        return datetime.datetime.strptime(date_, '%d %b %Y')

    def get_age(race_dob):
        race, dob = race_dob
        race, dob = get_date(race), get_date(date)
        return divmod((race - dob).days, 365.25)
    
    def get_race_times(line):
        return re.findall(r'\d{2}:\s+', line)[0]
    
    time = get_race_times(line)
    event_dob = re.findall(r'\d{2} \w{3} \d{4}', line)
    age = get_age(event_dob)
    return (age, time)


def get_slowest_age_times():
    races = input()
    race_age = []
    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
            race_age.append(get_event_time(line))
    slowest_race = max(race_age, key=lambda x: x[1])
    slowest_age, slowest_race_time = slowest_race

    def format_date(age):
        years, days = age
        return f'{int(years)}y{int(days)}d'
    
    return (format_date(slowest_age), slowest_race_time)