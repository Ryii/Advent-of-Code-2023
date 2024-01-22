def getLongestHike():
  lines = open('input.txt').read().splitlines()

  start = (0, lines[0].index("."))
  end = (len(lines) - 1, lines[-1].index("."))

  points = [start, end]

  for r, row in enumerate(lines):
    for c, ck in enumerate(row):
      if ck == "#":
        continue
      neighbors = 0
      for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]) and lines[nr][nc] != "#":
          neighbors += 1
        if neighbors >= 3:
          points.append((r, c))

  graph = {pt: {} for pt in points}

  dirs = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".":[(-1, 0), (1, 0), (0, -1), (0, 1)]
  }

  for sr, sc in points:
    stack = [(0, sr, sc)]
    seen = {(sr, sc)}

    while stack:
      n, r, c = stack.pop()

      if n != 0 and (r, c) in points:
        graph[(sr, sc)][(r,c)] = n
        continue

      for dr, dc in dirs[lines[r][c]]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]) and lines[nr][nc] != "#" and (nr, nc) not in seen:
          stack.append((n+1, nr, nc))
          seen.add((nr, nc))

  seen = set()

  def dfs(pt):
    if pt == end:
      return 0
    
    m = -float("inf")

    seen.add(pt)
    for nx in graph[pt]:
      m = max(m, dfs(nx) + graph[pt][nx])
    seen.remove(pt)

    return m
  
  print(dfs(start))



def getLongestHike2():
  lines = open('input.txt').read().splitlines()

  start = (0, lines[0].index("."))
  end = (len(lines) - 1, lines[-1].index("."))

  points = [start, end]

  for r, row in enumerate(lines):
    for c, ck in enumerate(row):
      if ck == "#":
        continue
      neighbors = 0
      for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]) and lines[nr][nc] != "#":
          neighbors += 1
        if neighbors >= 3:
          points.append((r, c))

  graph = {pt: {} for pt in points}

  for sr, sc in points:
    stack = [(0, sr, sc)]
    seen = {(sr, sc)}

    while stack:
      n, r, c = stack.pop()

      if n != 0 and (r, c) in points:
        graph[(sr, sc)][(r,c)] = n
        continue

      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(lines) and 0 <= nc < len(lines[0]) and lines[nr][nc] != "#" and (nr, nc) not in seen:
          stack.append((n+1, nr, nc))
          seen.add((nr, nc))

  seen = set()

  def dfs(pt):
    if pt == end:
      return 0
    
    m = -float("inf")

    seen.add(pt)
    for nx in graph[pt]:
      if nx not in seen:
        m = max(m, dfs(nx) + graph[pt][nx])
    seen.remove(pt)

    return m
  
  print(dfs(start))

getLongestHike2()