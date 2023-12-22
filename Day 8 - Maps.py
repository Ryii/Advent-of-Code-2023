import math

def getSteps():
  f = open("input.txt", "r")
  lines = f.read().splitlines()

  path = lines[0]
  nodeLines = lines[2:]
  pathMap = {}

  for line in nodeLines:
    node, left, right = line.split()[0], line.split()[2][1:4], line.split()[3][:3]
    pathMap[node] = (left, right)

  cur = 'AAA'
  steps = 0
  pathIndex = 0

  while cur != 'ZZZ':
    if pathIndex == len(path):
      pathIndex = 0

    cur = pathMap[cur][0] if path[pathIndex] == 'L' else pathMap[cur][1]
    steps += 1
    pathIndex += 1

  return steps

# print(getSteps())


def getGhostSteps():
  f = open("input.txt", "r")
  lines = f.read().strip().splitlines()

  path = lines[0]
  nodeLines = lines[2:]
  pathMap = {}
  nodes = []

  for line in nodeLines:
    node, left, right = line.split()[0], line.split()[2][1:4], line.split()[3][:3]
    pathMap[node] = (left, right)

    if node.endswith('A'):
      nodes.append(node)

  total = 1

  for node in nodes:
    steps = 0
    pathIndex = 0

    while not node.endswith('Z'):
      if pathIndex == len(path):
        pathIndex = 0

      node = pathMap[node][0] if path[pathIndex] == 'L' else pathMap[node][1]

      steps += 1
      pathIndex += 1

    total = math.lcm(steps, total)

  return total

print(getGhostSteps())