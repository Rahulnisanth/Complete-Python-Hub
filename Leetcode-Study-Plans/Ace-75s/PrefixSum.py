# FIND THE HIGHEST ALTITUDE :
def largestAltitude(gain) -> int:
    currentAltitude, highestPoint = 0, 0
    for altitude in gain:
        currentAltitude += altitude
        highestPoint = max(highestPoint, currentAltitude)
    return highestPoint