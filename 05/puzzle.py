def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  coords = line.strip().split(" -> ")
  coords[0] = coords[0].split(",")
  coords[1] = coords[1].split(",")
  return [(int(coords[0][0]), int(coords[0][1])), (int(coords[1][0]), int(coords[1][1]))]

def findHorizontalOrVertical(lines):
  return list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines))


def findOverlap(lines):
  seenOnce = set()
  seenMultiple = set()
  for line in lines:
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    xPointRange = range(x1, x2-1, -1) if x1 > x2 else range(x1, x2+1)
    yPointRange = range(y1, y2-1, -1) if y1 > y2 else range(y1, y2+1)

    if (len(xPointRange) == 1):
      # horizonal line
      xPointRange = [xPointRange[0]] * len(yPointRange)
    if (len(yPointRange) == 1):
      # vertical line
      yPointRange = [yPointRange[0]] * len(xPointRange)

    for pointIndex in range(len(xPointRange)):
      xPoint = xPointRange[pointIndex]
      yPoint = yPointRange[pointIndex]
      if ((xPoint, yPoint) in seenMultiple):
        continue
      if ((xPoint, yPoint) in seenOnce):
        seenMultiple.add((xPoint, yPoint))
        seenOnce.remove((xPoint, yPoint))
      else:
        seenOnce.add((xPoint, yPoint))
  return len(seenMultiple)

lines = readFileByLine()

# Part A
horizontalOrVerticalLines = findHorizontalOrVertical(lines)
print("Part A: Only horizontal or vertical - ", findOverlap(horizontalOrVerticalLines))

# Part B
print("Part B: All lines - ", findOverlap(lines))



