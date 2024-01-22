from collections import deque

def getBricks():
  lines = open('input.txt').read().splitlines()

  for i, line in enumerate(lines):
    lines[i] = list(map(int, line.replace("~", ",").split(",")))
  
  lines.sort(key=lambda line: line[2])

  def overlaps(x, y):
    return max(x[0], y[0]) <= min(x[3], y[3]) and max(x[1], y[1]) <= min(x[4], y[4])

  for i, line in enumerate(lines):
    maxz = 1
    for check in lines[:i]:
      if overlaps(line, check):
        maxz = max(maxz, check[5] + 1)

    line[5] -= line[2] - maxz
    line[2] = maxz

  lines.sort(key = lambda line: line[2])

  k_v = {i: set() for i in range(len(lines))}
  v_k = {i: set() for i in range(len(lines))}

  for i, upper in enumerate(lines):
    for j, lower in enumerate(lines[:i]):
      if overlaps(lower, upper) and upper[2] == lower[5] + 1:
        k_v[j].add(i)
        v_k[i].add(j)

  total = 0

  for i in range(len(lines)):
    if all(len(v_k[j]) >= 2 for j in k_v[i]):
      total += 1

  print(total)

def getBricks2():
  lines = open('input.txt').read().splitlines()

  for i, line in enumerate(lines):
    lines[i] = list(map(int, line.replace("~", ",").split(",")))
  
  lines.sort(key=lambda line: line[2])

  def overlaps(x, y):
    return max(x[0], y[0]) <= min(x[3], y[3]) and max(x[1], y[1]) <= min(x[4], y[4])

  for i, line in enumerate(lines):
    maxz = 1
    for check in lines[:i]:
      if overlaps(line, check):
        maxz = max(maxz, check[5] + 1)

    line[5] -= line[2] - maxz
    line[2] = maxz

  lines.sort(key = lambda line: line[2])

  k_v = {i: set() for i in range(len(lines))}
  v_k = {i: set() for i in range(len(lines))}

  for i, upper in enumerate(lines):
    for j, lower in enumerate(lines[:i]):
      if overlaps(lower, upper) and upper[2] == lower[5] + 1:
        k_v[j].add(i)
        v_k[i].add(j)

  total = 0

  for i in range(len(lines)):
    q = deque(j for j in k_v[i] if len(v_k[j]) == 1)
    falling = set(q)
    falling.add(i)

    while q:
      j = q.popleft()
      for k in k_v[j] - falling:
        if v_k[k] <= falling:
          q.append(k)
          falling.add(k)

    total += len(falling) - 1

  print(total)

getBricks2()