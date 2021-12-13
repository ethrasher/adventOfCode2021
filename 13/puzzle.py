def getDots():
  file1 = open('puzzleInput-dots.txt', 'r')
  lines = file1.readlines()
  dots = set()
  for line in lines:
    line = line.strip().split(",")
    dots.add((int(line[0]), int(line[1])))
  return dots

def getFolds():
  file1 = open('puzzleInput-folds.txt', 'r')
  lines = file1.readlines()
  folds = []
  for line in lines:
    fold = line.strip().split(" ")[-1]
    fold = fold.split("=")
    folds.append((fold[0]=="y", int(fold[1])))
  return folds

def performFold(allDots, fold):
  newDots = set()
  for dot in allDots:
    if (fold[0]):
      # folding up
      if (dot[1] < fold[1]):
        newDots.add(dot)
      else:
        yDelta = dot[1] - fold[1]
        newDots.add((dot[0], dot[1]-yDelta*2))
    else:
      #folding left/right
      if (dot[0] < fold[1]):
        newDots.add(dot)
      else:
        xDelta = dot[0]-fold[1]
        newDots.add((dot[0]-xDelta*2, dot[1]))
  return newDots

def printPaper(allDots):
  maxX = 0
  maxY = 0
  for dot in allDots:
    if dot[0] > maxY:
      maxY = dot[0]
    if dot[1] > maxX:
      maxX = dot[1]
  for x in range(maxX+1):
    for y in range(maxY+1):
      if ((y,x) in allDots):
        print("#", end='')
      else:
        print(".", end='')
    print()
  print()


allDots = getDots()
allFolds = getFolds()

dotsAfterFold1 = performFold(allDots, allFolds[0])
print("Part A - number of dots after 1 fold ", len(dotsAfterFold1))

for fold in allFolds:
  allDots = performFold(allDots, fold)
print("Part B - 8 capital letters below")
printPaper(allDots)








