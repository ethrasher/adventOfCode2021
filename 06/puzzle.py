def readFile():
  file1 = open('puzzleInput.txt', 'r')
  line = (file1.readlines())[0].split(",")
  return list(map(lambda x: int(x), line))

def createInitialLanternfish(lanternFishFromFile):
  lanternFish = [0]*9
  for fish in lanternFishFromFile:
      lanternFish[fish] +=1
  return lanternFish

def newDay(lanternFish):
  newLanternFish = [0]*9
  for i in range(len(lanternFish)-1):
      newLanternFish[i] = lanternFish[i+1]
  newLanternFish[8] = lanternFish[0]
  newLanternFish[6] += lanternFish[0]
  return newLanternFish

lanternFishFromFile = readFile()
# Part A
lanternFishPartA = createInitialLanternfish(lanternFishFromFile)
days = 80
for day in range(days):
  lanternFishPartA = newDay(lanternFishPartA)
print("Part A: 80 days - ", sum(lanternFishPartA))

# Part B
lanternFishPartB = createInitialLanternfish(lanternFishFromFile)
days = 256
for day in range(days):
  lanternFishPartB = newDay(lanternFishPartB)
print("Part B: 256 days - ", sum(lanternFishPartB))

