testStartingPoly = "NNCB"
startingPoly = "SFBBNKKOHHHPFOFFSPFV"

def getFormulas():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  formulas = dict()
  for line in lines:
    line = line.strip().split(" -> ")
    formulas[line[0]] = line[1]
  return formulas

def getStartingPoly(s):
  poly = dict()
  for i in range(len(s)-1):
    combo = s[i:i+2]
    if combo not in poly:
      poly[combo] = 0
    poly[combo] += 1
  return poly


def runStep(startingPoly, formulas):
  finalPoly = {}
  for combo in startingPoly:
    if combo not in formulas:
      print("NOT A FORMULA")
      finalPoly[combo] = startingPoly[combo]
    else:
      newCombo1 = combo[0]+formulas[combo]
      newCombo2 = formulas[combo] + combo[1]
      if newCombo1 not in finalPoly:
        finalPoly[newCombo1] = 0
      finalPoly[newCombo1] += startingPoly[combo]
      if newCombo2 not in finalPoly:
        finalPoly[newCombo2] = 0
      finalPoly[newCombo2] += startingPoly[combo]
  return finalPoly

def getCounts(poly, startingLetter):
  counts = dict()
  counts[startingLetter] = 1
  for combo in poly:
    if (combo[0] not in counts):
      counts[combo[0]] = 0
    #counts[combo[0]] -= poly[combo]
    if (combo[1] not in counts):
      counts[combo[1]] = 0
    counts[combo[1]] += poly[combo]
  return counts

startingPoly = startingPoly
poly = getStartingPoly(startingPoly)
formulas = getFormulas()
steps = 10
for step in range(steps):
  poly = runStep(poly, formulas)
counts = getCounts(poly, startingPoly[0])

print("Part A - 10 steps: ", max(counts.values()) - min(counts.values()))

steps = 30
for step in range(steps):
  poly = runStep(poly, formulas)
counts = getCounts(poly, startingPoly[0])

print("Part B - 40 steps: ", max(counts.values()) - min(counts.values()))




