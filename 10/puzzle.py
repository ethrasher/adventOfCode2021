def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  return line.strip()

fileLines = readFileByLine()

def getSyntaxPoints(line):
  pointValues = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
  }
  openCloseStack = []
  for c in line:
    if c in ["(", "[", "{", "<"]:
      # open
      openCloseStack.append(c)
    else:
      if len(openCloseStack) == 0:
        return pointValues[c]
      lastOpen = openCloseStack.pop(-1)
      if ((c == ")" and lastOpen != "(") or
          (c == "]" and lastOpen != "[") or
          (c == "}" and lastOpen != "{") or
          (c == ">" and lastOpen != "<")):
        return pointValues[c]
  return 0

def scoreAndRemoveCorruptLines(lines):
  total = 0
  nonCorruptLines = []
  for i in range(len(lines)):
    linePoints = getSyntaxPoints(lines[i])
    total += linePoints
    if linePoints == 0:
      nonCorruptLines.append(lines[i])
  return (total, nonCorruptLines)


(corruptLinesPoints, nonCorruptLines) = scoreAndRemoveCorruptLines(fileLines)

print("Part A - score for corrupt:", corruptLinesPoints)

def completeLinePoints(line):
  pointValues = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
  }
  openCloseStack = []
  for c in line:
    if c in ["(", "[", "{", "<"]:
      # open
      openCloseStack.append(c)
    else:
      openCloseStack.pop(-1)
  total = 0
  for i in range(len(openCloseStack)-1, -1, -1):
    currentOpen = openCloseStack[i]
    total *= 5
    total += pointValues[currentOpen]
  return total

incompleteScores = sorted(list(map(completeLinePoints, nonCorruptLines)))

print("Part B - score for incomplete:", incompleteScores[len(incompleteScores)//2])



