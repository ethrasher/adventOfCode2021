def readFileByLine():
  file1 = open('puzzleInput.txt', 'r')
  lines = file1.readlines()
  return list(map(lambda line: line.strip().split("-"), lines))


def makeCaveGraph(connections):
  caves = dict()
  for (nodeA, nodeB) in connections:
    if (nodeA not in caves):
      caves[nodeA] = set()
    if (nodeB not in caves):
      caves[nodeB] = set()
    caves[nodeA].add(nodeB)
    caves[nodeB].add(nodeA)
  return caves

def findAllPathsPartA(caves):
  allPaths = 0
  queue = [('start', set())]
  while (len(queue) > 0):
    caveName, seenSmallCaves = queue.pop(0)
    if (caveName == "end"):
      allPaths += 1
      continue
    newSeenSmallCaves = seenSmallCaves.copy()
    if (caveName.lower() == caveName):
      # small cave
      newSeenSmallCaves.add(caveName)
    for adjacentCave in caves[caveName]:
      if (adjacentCave not in newSeenSmallCaves):
        queue.append((adjacentCave, newSeenSmallCaves))
  return allPaths

def findAllPathsPartB(caves):
  allPaths = set()
  queue = [('start', set(["start"]), None, "")]
  while (len(queue) > 0):
    caveName, seenSmallCaves, seeTwice, path = queue.pop(0)
    if (caveName == "end"):
      allPaths.add(path+",end")
      continue
    if (caveName.lower() != caveName or caveName == "start"):
      # big cave
      for adjacentCave in caves[caveName]:
        if (adjacentCave not in seenSmallCaves):
          queue.append((adjacentCave, seenSmallCaves.copy(), seeTwice, path+","+caveName))
    else:
      # small cave
      for adjacentCave in caves[caveName]:
        if (adjacentCave not in seenSmallCaves):
          newSeenSmallCaves = seenSmallCaves.copy()
          newSeenSmallCaves.add(caveName)
          queue.append((adjacentCave, newSeenSmallCaves, seeTwice, path+","+caveName))
          if (seeTwice == None):
            # could lead to duplicates, need to de-dup paths at the end
            seenSmallCavesDup = seenSmallCaves.copy()
            queue.append((adjacentCave, seenSmallCavesDup, caveName, path+","+caveName))

  return len(allPaths)





connections = readFileByLine()
caves = makeCaveGraph(connections)

print("Part A - find all paths with small cave once:", findAllPathsPartA(caves))
print("Part B - find all paths repeat one small cave once:", findAllPathsPartB(caves))
