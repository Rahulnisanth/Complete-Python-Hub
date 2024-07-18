from collections import defaultdict

def convert_to_seconds(hh_mm_ss):
    hh, mm, ss = map(int, hh_mm_ss.split(':'))
    return (hh * 3600) + (mm * 60 )+ ss

def solve_problem(call_logs):
    durations = defaultdict(int)

    for log in call_logs:
        duration, phone_number = log.split(',')
        seconds = convert_to_seconds(duration)
        if phone_number in durations:
            durations[phone_number] += seconds
        else:
            durations[phone_number] = seconds

    max_duration = 0
    max_number_value = 0
    max_number = ""
    for number, duration in durations.items():
        if duration > max_duration:
            max_number = number
            max_number_value = int(number.replace("-",""))
            max_duration = duration
        else:
            if duration == max_duration:
                if int(number.replace("-","")) < max_number_value:
                    max_number = number
                    max_number_value = int(number.replace("-",""))

    total_cost = 0
    for phone_number, duration in durations.items():
        if phone_number == max_number:
            continue
        if duration > 300:
            total_cost += (duration // 60) * 150
            if duration % 60 != 0:
                total_cost += 150
        else:
            total_cost += duration * 3

    return total_cost


# Input drive :
call_logs = []
while True:
    try:
        buffer = input()
        if buffer == "": break
        call_logs.append(buffer.strip())
    except EOFError:
        break
print(call_logs)
print("Bill:", solve_problem(call_logs)) 
