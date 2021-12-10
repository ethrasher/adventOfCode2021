def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  line = list(line.strip())
  return list(map(lambda x: int(x), line))


def findLowPoints(heights):
  directions = [(1,0), (-1, 0), (0,1), (0, -1)]
  lowPoints = []
  for i in range(len(heights)):
    for j in range(len(heights[i])):
      isLowPoint = True
      center = heights[i][j]
      for direction in directions:
        if (i+direction[0] >= 0 and i+direction[0] < len(heights) and j+direction[1] >= 0 and j+direction[1] < len(heights[i])):
          adjacent = heights[i+direction[0]][j+direction[1]]
          if (adjacent <= center):
            isLowPoint = False
            break
      if isLowPoint:
        lowPoints.append((i, j))
  return lowPoints

def findRisk(lowPoints, heights):
  total = 0
  for lowPoint in lowPoints:
    total += heights[lowPoint[0]][lowPoint[1]]+1
  return total

heights = readFileByLine()
lowPoints = findLowPoints(heights)
print("Part A - find risk: ", findRisk(lowPoints, heights))

def findBasinSize(lowPoint, heights):
  seen = set()
  queue = [lowPoint]
  directions = [(1,0), (-1, 0), (0,1), (0, -1)]
  while (len(queue) > 0):
    current = queue.pop(0)
    seen.add(current)
    for direction in directions:
      newRow = current[0]+direction[0]
      newCol = current[1]+direction[1]
      if (newRow >= 0 and newRow < len(heights) and newCol >= 0 and newCol < len(heights[0])):
        if ((newRow, newCol) not in seen and heights[newRow][newCol] != 9):
          queue.append((newRow, newCol))
  return len(seen)

def multBiggestBasins(lowPoints, heights):
  basinSizes = list(map(lambda point: findBasinSize(point, heights), lowPoints))
  sortedBasins = sorted(basinSizes)
  return sortedBasins[-3]*sortedBasins[-2]*sortedBasins[-1]

print("Part B - biggest basins mult: ", multBiggestBasins(lowPoints, heights))




        


