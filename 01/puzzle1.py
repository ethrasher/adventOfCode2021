def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(lambda line: int(line.strip()), lines))

# Part A
def findNumberIncreases():
  depths = readFileByLine()
  count = 0
  previousDepth = None
  for depth in depths:
    if previousDepth != None and previousDepth < depth:
      count += 1
    previousDepth = depth
  return count

# print(findNumberIncreases(readFileByLine()))

# Part B
def findNumberIncreasesSlideWindow(depths):
  count = 0
  for i in range(1, len(depths)-2):
    window1 = depths[i-1:i+2]
    window2 = depths[i:i+3]
    if (sum(window1) < sum(window2)):
      count+=1
  return count

print(findNumberIncreasesSlideWindow(readFileByLine()))
