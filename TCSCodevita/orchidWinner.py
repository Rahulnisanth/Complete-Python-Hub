def CountPossibilities(arr):
    count = 0
    for i in range(0, len(arr) - 2):
        if arr[i] != arr[i + 1] and arr[i + 1] != arr[i + 2] and arr[i] != arr[i + 2]:
            count += 1
    return count


def findWinner(ashok, anand):
    ashokCount = CountPossibilities(ashok)
    anandCount = CountPossibilities(anand)
    if ashokCount > anandCount:
        return "Ashok"
    elif anandCount > ashokCount:
        return "Anand"
    else:
        return "Draw"
