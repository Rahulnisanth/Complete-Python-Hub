# MIN GROUPS FOR NON OVERLAPPING INTERVALS :
def minGroups(intervals) -> int:
    events = []
    for start, end in intervals:
        events.append([start, 1])
        events.append([end + 1, -1])

    events.sort(key=lambda x: (x[0], x[1]))
    currentGroup, maxGroup = 0, 0
    for event in events:
        currentGroup += event[1]
        if currentGroup > maxGroup:
            maxGroup = currentGroup

    return maxGroup
