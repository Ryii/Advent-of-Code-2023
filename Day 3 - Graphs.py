def countParts():
  f = open("input.txt", "r")
  grid = f.read().splitlines()

  rows, cols = len(grid), len(grid[0])
  total = 0
  visited = set()

  def bfs(r: int, c: int, value: int, touching: bool):
    visited.add((r, c))

    directions = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]

    for dr, dc in directions:
      if r+dr in range(rows) and c+dc in range(cols) and not grid[r+dr][c+dc] == "." and not grid[r+dr][c+dc].isnumeric():
        touching = True

    value += int(grid[r][c])

    if (c + 1 < cols) and grid[r][c+1].isnumeric():
      return bfs(r, c+1, value * 10, touching)
    else:
      return (value, touching) if touching else (0, touching)

  for r in range(rows):
    for c in range(cols):
      if grid[r][c].isnumeric() and (r, c) not in visited:
        val, added = bfs(r, c, 0, False)
        print(added, val)
        total += bfs(r, c, 0, False)[0]

  return total

# print(countParts())


def countGears():
  f = open("input.txt", "r")
  grid = f.read().splitlines()

  rows, cols = len(grid), len(grid[0])
  total = 0
  visited = set()
  gearsMap = {}
  # (r, c): (count, value)

  def bfs(r: int, c: int, value: int, gears: list):
    visited.add((r, c))

    directions = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]

    for dr, dc in directions:
      if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == "*" and (r+dr, c+dc) not in gears:
        gears.append((r+dr, c+dc))

    value += int(grid[r][c])

    if (c + 1 < cols) and grid[r][c+1].isnumeric():
      bfs(r, c+1, value * 10, gears)
    else:
      for gear in gears:
        row, col = gear[0], gear[1]
        gearsMap[(row, col)] = (gearsMap.get((row, col), (0, 1))[0] + 1, gearsMap.get((row, col), (0, 1))[1] * value)

  for r in range(rows):
    for c in range(cols):
      if grid[r][c].isnumeric() and (r, c) not in visited:
        bfs(r, c, 0, [])

  for count, value in gearsMap.values():
    if count == 2:
      total += value

  return total

print(countGears())