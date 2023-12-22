def getArea():
  points = [(0, 0)]
  dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

  b = 0

  for line in open("input.txt").read().splitlines():
    direction, length, color = line.split()
    length = int(length)
    dr, dc = dirs[direction]
    r, c = points[-1]
    b += length
    points.append((r + dr*length, c + dc*length))

  area = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) // 2
  i = area - b // 2 + 1

  print(i + b)


def getAreaColor():
  points = [(0, 0)]
  dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

  b = 0

  for line in open("input.txt").read().splitlines():
    color = line.split()[2]
    color = color[2:-1]
    dr, dc = dirs["RDLU"[int(color[-1])]]
    length = int(color[:-1], 16)
    b += length
    r, c = points[-1]
    points.append((r + dr*length, c + dc*length))

  area = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) // 2
  i = area - b // 2 + 1

  print(i + b)

getAreaColor()