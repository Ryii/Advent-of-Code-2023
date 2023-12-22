from itertools import combinations

def getShortestSum():
  lines = open("input.txt").read().splitlines()
  ROWS, COLS = len(lines), len(lines[0])

  galaxies = []
  emptyRows = [1] * ROWS
  emptyCols = [1] * COLS

  for r in range(ROWS):
    for c in range(COLS):
      if lines[r][c] == "#":
        galaxies.append((r, c))
        emptyRows[r] = 0
        emptyCols[c] = 0

  rowPrefix = [emptyRows[0]] * ROWS
  colPrefix = [emptyCols[0]] * COLS

  for i in range(1, ROWS):
    rowPrefix[i] = rowPrefix[i - 1] + emptyRows[i]
  for i in range(1, COLS):
    colPrefix[i] = colPrefix[i - 1] + emptyCols[i]
  
  total = 0

  for g1, g2 in [pair for pair in combinations(galaxies, 2)]:
    
    total += abs(g2[0] - g1[0]) + abs(rowPrefix[g2[0]] - rowPrefix[g1[0]])
    total += abs(g2[1] - g1[1]) + abs(colPrefix[g2[1]] - colPrefix[g1[1]])

  return total

# print(getShortestSum())


def getShortestMillionSum():
  lines = open("input.txt").read().splitlines()
  ROWS, COLS = len(lines), len(lines[0])

  galaxies = []
  emptyRows = [999999] * ROWS
  emptyCols = [999999] * COLS

  for r in range(ROWS):
    for c in range(COLS):
      if lines[r][c] == "#":
        galaxies.append((r, c))
        emptyRows[r] = 0
        emptyCols[c] = 0

  rowPrefix = [emptyRows[0]] * ROWS
  colPrefix = [emptyCols[0]] * COLS

  for i in range(1, ROWS):
    rowPrefix[i] = rowPrefix[i - 1] + emptyRows[i]
  for i in range(1, COLS):
    colPrefix[i] = colPrefix[i - 1] + emptyCols[i]
  
  total = 0

  for g1, g2 in [pair for pair in combinations(galaxies, 2)]:
    
    total += abs(g2[0] - g1[0]) + abs(rowPrefix[g2[0]] - rowPrefix[g1[0]])
    total += abs(g2[1] - g1[1]) + abs(colPrefix[g2[1]] - colPrefix[g1[1]])

  return total

print(getShortestMillionSum())