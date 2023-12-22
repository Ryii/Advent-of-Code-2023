from collections import deque

def getEnergized():
  grid = open("input.txt").read().splitlines()
  ROWS, COLS = len(grid), len(grid[0])

  # r, c, dr, dc
  a = [(0, -1, 0, 1)]
  visited = set()
  q = deque(a)

  while q:
    r, c, dr, dc = q.popleft()

    r += dr
    c += dc

    if r not in range(ROWS) or c not in range(COLS):
      continue

    char = grid[r][c]

    if char == '.' or (char == "-" and dc != 0) or (char == "|" and dr != 0):
      if (r, c, dr, dc) not in visited:
        visited.add((r, c, dr, dc))
        q.append((r, c, dr, dc))

    elif char == "/":
      dr, dc = -dc, -dr
      if (r, c, dr, dc) not in visited:
        visited.add((r, c, dr, dc))
        q.append((r, c, dr, dc))
    elif char == "\\":
      dr, dc = dc, dr
      if (r, c, dr, dc) not in visited:
        visited.add((r, c, dr, dc))
        q.append((r, c, dr, dc))
    else:
      for dr, dc, in [(1, 0), (-1, 0)] if char == "|" else [(0, 1), (0, -1)]:
        if (r, c, dr, dc) not in visited:
          visited.add((r, c, dr, dc))
          q.append((r, c, dr, dc))

  coords = {(r, c) for (r, c, _, _) in visited}

  print(len(coords))

def getEnergizedConfig():
  grid = open("input.txt").read().splitlines()
  ROWS, COLS = len(grid), len(grid[0])

  def calc(r, c, dr, dc):

    a = [(r, c, dr, dc)]
    visited = set()
    q = deque(a)

    while q:
      r, c, dr, dc = q.popleft()

      r += dr
      c += dc

      if r not in range(ROWS) or c not in range(COLS):
        continue

      char = grid[r][c]

      if char == '.' or (char == "-" and dc != 0) or (char == "|" and dr != 0):
        if (r, c, dr, dc) not in visited:
          visited.add((r, c, dr, dc))
          q.append((r, c, dr, dc))

      elif char == "/":
        dr, dc = -dc, -dr
        if (r, c, dr, dc) not in visited:
          visited.add((r, c, dr, dc))
          q.append((r, c, dr, dc))
      elif char == "\\":
        dr, dc = dc, dr
        if (r, c, dr, dc) not in visited:
          visited.add((r, c, dr, dc))
          q.append((r, c, dr, dc))
      else:
        for dr, dc, in [(1, 0), (-1, 0)] if char == "|" else [(0, 1), (0, -1)]:
          if (r, c, dr, dc) not in visited:
            visited.add((r, c, dr, dc))
            q.append((r, c, dr, dc))

    coords = {(r, c) for (r, c, _, _) in visited}

    return len(coords)

  max_val = 0

  for r in range(ROWS):
    max_val = max(max_val, calc(r, -1, 0, 1), calc(r, COLS, 0, -1))

  for c in range(COLS):
    max_val = max(max_val, calc(-1, c, 1, 0), calc(ROWS, c, -1, 0))

  print(max_val)

getEnergizedConfig()