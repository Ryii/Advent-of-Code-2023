def totalLoad():
  lines = open("input.txt").read().splitlines()
  cols = list(zip(*lines))

  total = 0

  for col in cols:
    colSum = 0
    rocks = 0

    for c, char in enumerate(col[::-1], 1):
      if char == "O":
        rocks += 1
      elif char == "#":
        for r in range(1, rocks + 1):
          colSum += (c - r)
        rocks = 0
      
    for r in range(rocks):
      colSum += (len(col) - r)

    total += colSum

  return total


def spinMillionTimes():
  lines = tuple(open("input.txt").read().splitlines())

  def cycle():
    nonlocal lines
    for i in range(4):
      lines = tuple(map("".join, zip(*lines)))
      lines = tuple("#".join(["".join(sorted(tuple(string), reverse=True)) for string in row.split("#")]) for row in lines)
      lines = tuple(line[::-1] for line in lines)

  seen = {lines}
  array = [lines]

  iter = 0

  while True:
    iter += 1
    cycle()
    if lines in seen:
      break
    seen.add(lines)
    array.append(lines)

  first = array.index(lines)

  lines = array[(1000000000 - first) % (iter - first) + first]

  return sum(line.count("O") * (len(lines) - r) for r, line in enumerate(lines))


print(spinMillionTimes())

