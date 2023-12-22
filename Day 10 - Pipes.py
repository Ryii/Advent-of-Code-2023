def getLongestDistance():
  f = open("input.txt")
  lines = f.read().splitlines()

  ROWS = len(lines)
  COLS = len(lines[0])
  UP, RIGHT, DOWN, LEFT = 1, 2, 3, 4

  S = (-1, -1)
  facingDirection = 0
  startingPipe = "|"

  # Get S position and facingDirection
  for r, line in enumerate(lines):
    for c, char in enumerate(line):
      if char == "S":
        S = (r, c)
        if (r+1 in range(ROWS) and c in range(COLS) and lines[r+1][c] == "|" or lines[r+1][c] == "J" or lines[r+1][c] == "L"): 
          facingDirection, startingPipe = DOWN, lines[r+1][c]
        elif (r-1 in range(ROWS) and c in range(COLS) and lines[r-1][c] == "|" or lines[r-1][c] == "F" or lines[r-1][c] == "7"): 
          facingDirection, startingPipe = UP, lines[r-1][c]
        else:
          facingDirection, startingPipe = RIGHT, lines[r][c+1]
    if S != (-1, -1):
      break

  
  # Pipe: { curFacingDirection: (nextPosX, nextPosY, nextFacingDirection) }
  moveHash = {"|": {UP: (-1, 0, UP), DOWN: (1, 0, DOWN)},
              "-": {RIGHT: (0, 1, RIGHT), LEFT: (0, -1, LEFT)},
              "L": {DOWN: (0, 1, RIGHT), LEFT: (-1, 0, UP)},
              "J": {RIGHT: (-1, 0, UP), DOWN: (0, -1, LEFT)},
              "7": {UP: (0, -1, LEFT), RIGHT: (1, 0, DOWN)},
              "F": {UP: (0, 1, RIGHT), LEFT: (1, 0, DOWN)}}

    
  curPos = (S[0] + moveHash[startingPipe][facingDirection][0], 
            S[1]+ moveHash[startingPipe][facingDirection][1])
  facingDirection = moveHash[startingPipe][facingDirection][2]

  totalSteps = 1

  while curPos != S:
    symbol = lines[curPos[0]][curPos[1]]
    curPos = (curPos[0] + moveHash[symbol][facingDirection][0], 
            curPos[1]+ moveHash[symbol][facingDirection][1])
    facingDirection = moveHash[symbol][facingDirection][2]
    totalSteps += 1

  return totalSteps // 2


# print(getLongestDistance())



def getNumber():
  f = open("input.txt")
  lines = f.read().splitlines()

  ROWS = len(lines)
  COLS = len(lines[0])
  UP, RIGHT, DOWN, LEFT = 1, 2, 3, 4

  S = (-1, -1)
  facingDirection = 0
  startingPipe = "|"

  # Get S position and facingDirection, replace S
  for r, line in enumerate(lines):
    for c, char in enumerate(line):
      if char == "S":
        S = (r, c)
        if (lines[r+1][c] == "|" or lines[r+1][c] == "J" or lines[r+1][c] == "L"):
          if (lines[r][c-1] == "-" or lines[r][c-1] == "F" or lines[r][c-1] == "L"):
            lines[r] = line[:c] + "7" + line[c+1:]
          elif (lines[r-1][c] == "|" or lines[r-1][c] == "7" or lines[r-1][c] == "F"):
            lines[r] = line[:c] + "|" + line[c+1:]
          else:
            lines[r] = line[:c] + "F" + line[c+1:]
          facingDirection = UP
        elif (lines[r][c-1] == "-" or lines[r][c-1] == "F" or lines[r][c-1] == "L"):
          if (lines[r-1][c] == "|" or lines[r-1][c] == "7" or lines[r-1][c] == "F"):
            lines[r] = line[:c] + "J" + line[c+1:]
          else:
            lines[r] = line[:c] + "-" + line[c+1:]
          facingDirection = RIGHT
        else:
          lines[r] = line[:c] + "L" + line[c+1:]
          facingDirection = DOWN

        # if (r+1 in range(ROWS) and c in range(COLS) and (lines[r+1][c] == "|" or lines[r+1][c] == "J" or lines[r+1][c] == "L")): 
        #   facingDirection, startingPipe = DOWN, lines[r+1][c]
        # elif (r-1 in range(ROWS) and c in range(COLS) and (lines[r-1][c] == "|" or lines[r-1][c] == "F" or lines[r-1][c] == "7")): 
        #   facingDirection, startingPipe = UP, lines[r-1][c]
        # else:
        #   facingDirection, startingPipe = RIGHT, lines[r][c+1]
    if S != (-1, -1):
      break

  
  # Pipe: { curFacingDirection: (nextPosX, nextPosY, nextFacingDirection) }
  moveHash = {"|": {UP: (-1, 0, UP), DOWN: (1, 0, DOWN)},
              "-": {RIGHT: (0, 1, RIGHT), LEFT: (0, -1, LEFT)},
              "L": {DOWN: (0, 1, RIGHT), LEFT: (-1, 0, UP)},
              "J": {RIGHT: (-1, 0, UP), DOWN: (0, -1, LEFT)},
              "7": {UP: (0, -1, LEFT), RIGHT: (1, 0, DOWN)},
              "F": {UP: (0, 1, RIGHT), LEFT: (1, 0, DOWN)}}
  
  
  curPos = S

  borderSet = set()
  # borderSet.append(S)
  # borderSet.append(curPos)
  numInside = 0

  # print('Starting: ', curPos, facingDirection)
  
  while curPos not in borderSet:
    borderSet.add(curPos)

    symbol = lines[curPos[0]][curPos[1]]
    curPos = (curPos[0] + moveHash[symbol][facingDirection][0], 
            curPos[1]+ moveHash[symbol][facingDirection][1])
    facingDirection = moveHash[symbol][facingDirection][2]

  for r, line in enumerate(lines):
    inside = False
    startFlag = 0   # -1 represents "F", 1 represents "L"
    LFlag = False
    for c, char in enumerate(line):
      if (r, c) not in borderSet and inside == True:
        numInside += 1
      if (r, c) in borderSet:
        if lines[r][c] == "F":
          startFlag = -1
        elif lines[r][c] == "L":
          startFlag = 1
        elif lines[r][c] == "7":
          inside = not inside if startFlag == 1 else inside
        elif lines[r][c] == "J":
          inside = not inside if startFlag == -1 else inside
        elif lines[r][c] == "|":
          inside = not inside

  return numInside


print(getNumber())