class Octopus:
  def __init__ (self, row, col, startingEnergy):
    self.row = row;
    self.col = col;
    self.energy = startingEnergy
    self.flashed = False
    self.adjacent = []

  def __repr__ (self):
    return str(self.energy)

  def resetFlash (self):
    if (self.flashed):
      self.flashed = False
      self.energy = 0
      return 1
    else:
      return 0

  def increaseEnergy(self):
    if (not self.flashed):
      self.energy += 1
      if (self.energy == 10):
        self.flashed = True
        for adjacentOctopus in self.adjacent:
          adjacentOctopus.increaseEnergy()

def printOctoBoard(octopusBoard):
  for i in range(len(octopusBoard)):
    for j in range(len(octopusBoard[0])):
      octopus = octopusBoard[i][j]
      print(octopus, end="")
    print()
  print()

def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  octopusBoard = []
  for row in range(len(lines)):
    octopusBoard.append(formatLine(row, lines[row]))
  return octopusBoard

def formatLine(row, line):
  octopusEnergy = list(line.strip())
  octopusRow = []
  for col in range(len(octopusEnergy)):
    octopusRow.append(Octopus(row, col, int(octopusEnergy[col])))
  return octopusRow


def setAdjacent(octopusBoard):
  directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  for i in range(len(octopusBoard)):
    for j in range(len(octopusBoard[0])):
      octopus = octopusBoard[i][j]
      for direction in directions:
        newRow = i + direction[0]
        newCol = j + direction[1]
        if (newRow >= 0 and newRow < len(octopusBoard) and newCol >= 0 and newCol < len(octopusBoard[0])):
          octopus.adjacent.append(octopusBoard[newRow][newCol])


def runStep(octopusBoard):
  directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
  queue = []
  for i in range(len(octopusBoard)):
    for j in range(len(octopusBoard[0])):
      octopus = octopusBoard[i][j]
      octopus.increaseEnergy()

  flashes = 0
  allFlashed = True
  for i in range(len(octopusBoard)):
    for j in range(len(octopusBoard[0])):
      octopus = octopusBoard[i][j]
      flashed = octopus.resetFlash()
      flashes += flashed
      allFlashed = allFlashed and flashed

  return (flashes, allFlashed)


octopusBoard = readFileByLine()
setAdjacent(octopusBoard)
steps = 100
totalFlashes = 0
for step in range(steps):
  flashes, allFlashed = runStep(octopusBoard)
  totalFlashes += flashes
print("Part A - total flashes after 100 steps", totalFlashes)

octopusBoard = readFileByLine()
setAdjacent(octopusBoard)
stepCounter = 0
while (True):
  stepCounter += 1
  flashes, allFlashed = runStep(octopusBoard)
  if allFlashed:
    break;
print("Part B - steps until all flash", stepCounter)



