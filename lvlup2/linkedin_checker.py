import re


def get_linkedin_dict():
    ''''''
    data = {}
    minimum, maximum = 0, 0
    regex = ''
    for line in specifications.splitlines():
        if line:
            if 'Requirements' in line:
                minimum, maximum = re.findall(r'\d+', line)
                minimum = int(minimum)
                maximum = int(maximum)
            elif 'Permitted characters' in line:
                regex = ''.join(line.split()[2:])
                regex = re.compile(rf'^[{regex}]+$')
            elif 'login characters' in line:
                regex = ''.join(line.split()[2:])
                regex = regex[::-1]
                regex = regex.replace('.', '.\\', 1).replace('-', '-\\', 1)
            else:
                feature = line.split()[-1]
            data[feature] = specs(range(minimum, maximum + 1), regex)
    return data