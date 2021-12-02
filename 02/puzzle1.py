def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line): 
  line = line.strip().split(" ")
  line[1] = int(line[1])
  return line


# Part A
def getFinalPositonA(instructions):
  horizontalPos = 0
  depth = 0
  for [movement, amount] in instructions:
    if (movement == "forward"):
        horizontalPos += amount
    if (movement == "down"):
        depth += amount
    if (movement == "up"):
        depth -= amount
  return horizontalPos*depth

#print(getFinalPositonA(readFileByLine()))


# Part B
def getFinalPositonB(instructions):
  horizontalPos = 0
  aim = 0
  depth = 0
  for [movement, amount] in instructions:
    print(movement, amount)
    if (movement == "forward"):
      horizontalPos += amount
      depth += aim*amount
    if (movement == "down"):
      aim += amount
    if (movement == "up"):
      aim -= amount
    print(horizontalPos, aim, depth)
  return horizontalPos*depth

print(getFinalPositonB(readFileByLine()))