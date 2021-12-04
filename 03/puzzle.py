import copy

def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  return line.strip()

def turnToDecimal(binary):
  total = 0
  for i in range(len(binary)):
    total += binary[len(binary)-i-1] * 2**i
  return total


# Part A
def getPowerConsumption(report):
  frequencyPosition = [[0,0] for i in range(len(report[0]))]
  for line in report:
    for i in range(len(line)):
      frequencyPosition[i][int(line[i])] += 1
  gamma = list(map(lambda freq: int(freq[1]>freq[0]), frequencyPosition))
  epsilon = list(map(lambda freq: int(freq[1]<freq[0]), frequencyPosition))
  return turnToDecimal(gamma) * turnToDecimal(epsilon)

#print(getPowerConsumption(readFileByLine()))

# Part B
def getMostCommon(report, bitPosition):
  freq = [0,0]
  for line in report:
    freq[int(line[bitPosition])] += 1
  return int(freq[1] >= freq[0])

def getOxygenGen(options):
  bitPosition = 0
  while (len(options) > 1):
    mostCommon = getMostCommon(options, bitPosition)
    options = list(filter(lambda option: int(option[bitPosition]) == mostCommon, options))
    bitPosition += 1
  return options[0]

def getCO2Scrub(options):
  bitPosition = 0
  while (len(options) > 1):
    mostCommon = getMostCommon(options, bitPosition)
    options = list(filter(lambda option: int(option[bitPosition]) != mostCommon, options))
    bitPosition += 1
  return options[0]

def getLifeSupportRating(report):
  oxygen = map(lambda i: int(i), getOxygenGen(copy.copy(report)))
  co2 = map(lambda i: int(i), getCO2Scrub(copy.copy(report)))
  return turnToDecimal(list(oxygen)) * turnToDecimal(list(co2))



print(getLifeSupportRating(readFileByLine()))