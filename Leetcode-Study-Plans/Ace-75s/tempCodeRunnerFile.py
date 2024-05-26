def numberRectangles(rectangles : list[list[int]]) -> int :
    sideOfSquares = []
    for i in range(len(rectangles)):
        sideOfSquares.append(min(rectangles[i]))

    maxNumberOfRectangles = 0
    for i in range(len(rectangles)):
        maxNumberOfRectangles += rectangles[i].count(max(sideOfSquares)) if min(rectangles[i]) == max(sideOfSquares) else 0
    return maxNumberOfRectangles

print(numberRectangles([[5,12],[3,5],[5,16],[20,5]]))