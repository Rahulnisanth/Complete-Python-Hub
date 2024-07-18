def count_successful_attacks(input_string):
    wall_heights = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    result = 0

    input_string = input_string.replace('−', '-')
    days = input_string.split(';')

    for day in days:
        attacks = day.split('$')[1].strip().split(':')
        heights = {'N': 0, 'S': 0, 'E': 0, 'W': 0}

        for attack in attacks:
            parts = attack.strip().split('-')
            tribe = parts[0].strip()
            direction = parts[1].strip()
            weapon = parts[2].strip()
            strength = int(parts[3].strip())

            if wall_heights[direction] < strength:
                result += 1

            heights[direction] = max(heights[direction], strength)

        for direction in wall_heights:
            wall_heights[direction] = max(wall_heights[direction], heights[direction])

    return result


# Input drive :
input_string = input()
print(count_successful_attacks(input_string)) 