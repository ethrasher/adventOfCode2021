def readFile():
  file1 = open('puzzleInput.txt', 'r')
  line = (file1.readlines())[0].split(",")
  return list(map(lambda x: int(x), line))

def distanceFromMedian(medianLocation, allLocations):
  total = 0
  for loc in allLocations:
    total += abs(loc - medianLocation)
  return total

crabLocations = sorted(readFile())
medianCrabLocation = crabLocations[len(crabLocations)//2]
print("Part A: 1 fuel - ", distanceFromMedian(medianCrabLocation, crabLocations))

saveSummations = dict()

def summationFuel(center, allLocations):
  total = 0
  for loc in allLocations:
    distance = abs(center-loc)+1
    if (distance in saveSummations):
      total += saveSummations[distance]
    else:
      fuel = sum(range(distance))
      total += fuel
      saveSummations[distance] = fuel
  return total

def bestPosition(allLocations):
  best = None
  for loc in range(min(allLocations), max(allLocations)):
    localTotal = summationFuel(loc, allLocations)
    if (best == None or localTotal < best):
      best = localTotal
  return best

print("Part B: increasing fuel - ", bestPosition(crabLocations))