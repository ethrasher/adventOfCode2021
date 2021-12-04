import copy

inputFile = "puzzleInput"

def getCalls(fileName):
  file1 = open(fileName, 'r')
  lines = file1.readlines()
  assert(len(lines) == 1)
  return list(map(lambda x: int(x), lines[0].strip().split(",")))

def getBoards(fileName):
  file1 = open(fileName, 'r')
  lines = file1.readlines()
  boards = []
  for i in range(0, len(lines), 6):
    boardLines = lines[i:i+5]
    board = []
    for boardLine in boardLines:
      row = list(map(lambda x: int(x), boardLine.split()))
      board.append(row)
    boards.append(board)
  return boards

def isBoardCompleted(board):
  # check rows
  for row in range(len(board)):
    completedRow = True
    for col in range(len(board[row])):
      if board[row][col] != None:
        completedRow = False
        break
    if completedRow:
      return True
  # check cols
  for col in range(len(board[0])):
    completedCol = True
    for row in range(len(board)):
      if board[row][col] != None:
        completedCol = False
        break
    if completedCol:
      return True
  return False

def getCompletedBoard(boards):
  for boardIndex in range(len(boards)):
    if (isBoardCompleted(boards[boardIndex])):
      return (boards[boardIndex], boardIndex)
  return None

def removeCompletedBoards(boards):
  return list(filter(lambda board: not isBoardCompleted(board), boards))

def callNumberForBoard(num, board):
  for row in range(len(board)):
    for col in range(len(board[0])):
      if (board[row][col] == num):
        board[row][col] = None

def callNumber(num, boards):
  for board in boards:
    callNumberForBoard(num,board)
  completed = getCompletedBoard(boards)
  if (completed != None):
    return (num, completed)
  return None

def evaluateCompletedBoard(call, board):
  total = 0
  for row in board:
    for num in row:
      if (num != None):
        total += num
  return total * call


calls = getCalls(inputFile + "-calls.txt")
boards = getBoards(inputFile + "-boards.txt")
foundWinner = False
for call in calls:
  completed = callNumber(call, boards)
  if (completed != None):
    lastCallNum = completed[0]
    completedBoard = completed[1][0]
    completedBoardIndex = completed[1][1]
    if (foundWinner == False):
      print("Part A: First to win - ", evaluateCompletedBoard(completed[0], completed[1][0]))
      foundWinner = True
    if (len(boards) == 1):
      print("Part B: Last to win - ", evaluateCompletedBoard(completed[0], completed[1][0]))
      break
    boards = removeCompletedBoards(boards)

