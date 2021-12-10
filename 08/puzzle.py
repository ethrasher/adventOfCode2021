def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(formatLine, lines))

def formatLine(line):
  (inputSigsString, outputSegsString) = line.strip().split(" | ")
  inputSigs = inputSigsString.split(" ")
  outputSegs = outputSegsString.split(" ")
  return (inputSigs, outputSegs)

displays = readFileByLine()

def count1478(displays):
  total = 0
  for display in displays:
    outputSegs = display[1]
    for outputSeg in outputSegs:
      if len(outputSeg) == 2 or len(outputSeg) == 4 or len(outputSeg) == 3 or len(outputSeg) == 7:
        total += 1
  return total

print("Part A - number of 1, 4, 7, 8: ", count1478(displays))

def sumUpDisplays(displays):
  allDisplayOutputs = list(map(lambda display: getDisplayOutput(display), displays))
  return sum(allDisplayOutputs)

def getDisplayOutput(display):
  weirdToProperSegMap = buildSegTranslation(display[0])
  outputs = display[1]
  total = 0
  for i in range(len(outputs)):
    intChar = translateOutputCharacter(outputs[i], weirdToProperSegMap)
    total += intChar*(10**(3-i))
  return total

def translateOutputCharacter(outputString, weirdToProperSegMap):
  translateProperSegToNum = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
  }
  properOutputString = ""
  for c in outputString:
    properOutputString += weirdToProperSegMap[c]
  properOutputString = ''.join(sorted(list(properOutputString)))
  return translateProperSegToNum[properOutputString]

def buildSegTranslation(inputs):
  weirdToProperSegMap = {
    "a": getValTranslation("a", inputs),
    "b": getValTranslation("b", inputs),
    "c": getValTranslation("c", inputs),
    "d": getValTranslation("d", inputs),
    "e": getValTranslation("e", inputs),
    "f": getValTranslation("f", inputs),
    "g": getValTranslation("g", inputs),
  }
  return weirdToProperSegMap

def getValTranslation(val, inputs):
  input4 = list(filter(lambda inputString: len(inputString) == 4, inputs))[0]
  matchingInputs = list(filter(lambda inputString: val in inputString, inputs))
  if (len(matchingInputs) == 6):
    return "b"
  if (len(matchingInputs) == 4):
    return "e"
  if (len(matchingInputs) == 9):
    return "f"
  if (len(matchingInputs) == 8):
    if (val in input4):
      return "c"
    else:
      return "a"
  if (len(matchingInputs) == 7):
    if (val in input4):
      return "d"
    else:
      return "g"
  print("ERROR CANNOT FIND")



# a -> count 8 (in 7)
# c -> count 8 (in 1, 4, 7)

# d -> count 7 (in 4)
# g -> count 7 (in none)

# b -> count 6
# e -> count 4
# f -> count 9

print("Part B - sum of all outputs: ", sumUpDisplays(displays))


