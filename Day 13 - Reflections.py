def getNoteSum():
  graphs = open("input.txt").read().split("\n\n")

  def getMirror(grid):
    for r in range(1, len(grid)):
      above = grid[:r][::-1]
      below = grid[r:]

      # makes them equal to the shorter between the two
      above = above[:len(below)]
      below = below[:len(above)]

      if above == below:
        return r
    return 0
      
  total = 0

  for graph in graphs:
    grid = graph.splitlines()
    row = getMirror(grid)
    total += row * 100

    col = getMirror(list(zip(*grid)))
    total += col

  print(total)


def getNoteSumSmudged():
  graphs = open("input.txt").read().split("\n\n")

  def getMirror(grid):
    for r in range(1, len(grid)):
      above = grid[:r][::-1]
      below = grid[r:]

      # makes them equal to the shorter between the two
      above = above[:len(below)]
      below = below[:len(above)]

      if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
        return r
    return 0
      
  total = 0

  for graph in graphs:
    grid = graph.splitlines()
    row = getMirror(grid)
    total += row * 100

    col = getMirror(list(zip(*grid)))
    total += col

  print(total)


getNoteSumSmudged()