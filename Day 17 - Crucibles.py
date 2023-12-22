import heapq

def getMinHeatLoss():
  grid = [list(map(int, row)) for row in open("input.txt").read().splitlines()]
  ROWS, COLS = len(grid), len(grid[0])

  visited = set()
  priority_q = [(0, 0, 0, 0, 0, 0)]

  while priority_q:
    hl, r, c, dr, dc, n = heapq.heappop(priority_q)

    if r == ROWS - 1 and c == COLS - 1:
      print(hl)
      break

    if r not in range(ROWS) or c not in range(COLS) or (r, c, dr, dc, n) in visited:
      continue

    visited.add((r, c, dr, dc, n))

    if n < 3 and (dr, dc) != (0, 0):
      nr = r + dr
      nc = c + dc
      if nr in range(ROWS) and nc in range(COLS):
        heapq.heappush(priority_q, (hl + grid[nr][nc], nr, nc, dr, dc, n+1))

    for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
        nr = r + ndr
        nc = c + ndc
        if nr in range(ROWS) and nc in range(COLS):
          heapq.heappush(priority_q, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


def getMinHeatLossUltra():
  grid = [list(map(int, row)) for row in open("input.txt").read().splitlines()]
  ROWS, COLS = len(grid), len(grid[0])

  visited = set()
  priority_q = [(0, 0, 0, 0, 0, 0)]

  while priority_q:
    hl, r, c, dr, dc, n = heapq.heappop(priority_q)

    if r == ROWS - 1 and c == COLS - 1 and n >= 4:
      print(hl)
      break

    if r not in range(ROWS) or c not in range(COLS) or (r, c, dr, dc, n) in visited:
      continue

    visited.add((r, c, dr, dc, n))

    if n < 10 and (dr, dc) != (0, 0):
      nr = r + dr
      nc = c + dc
      if nr in range(ROWS) and nc in range(COLS):
        heapq.heappush(priority_q, (hl + grid[nr][nc], nr, nc, dr, dc, n+1))

    if n >= 4 or (dr, dc) == (0, 0):
      for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
          nr = r + ndr
          nc = c + ndc
          if nr in range(ROWS) and nc in range(COLS):
            heapq.heappush(priority_q, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))

getMinHeatLossUltra()