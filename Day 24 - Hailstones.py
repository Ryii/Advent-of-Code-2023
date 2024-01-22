import sympy

def getIntersections():

  lines = open('input.txt').read().splitlines()
  hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in lines]

  total = 0

  for i, h1 in enumerate(hailstones):
    for h2 in hailstones[:i]:
      px, py = sympy.symbols("px py")
      sols = sympy.solve([vy * (px - sx) - vx * (py - sy) for sx, sy, _, vx, vy, _ in [h1, h2]])
      if sols == []:
        continue
      x, y = sols[px], sols[py]
      if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
        if all((x - sx) * vx >= 0 and (y - sy) * vy >= 0 for sx, sy, _, vx, vy, _ in [h1, h2]):
          total += 1

  print(total)

# getIntersections()


def getIntersections2():

  lines = open('input.txt').read().splitlines()
  hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in lines]

  xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

  equations = []

  for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
      continue
    answers = [sol for sol in sympy.solve(equations) if all(x % 1 == 0 for x in sol.values())]
    if len(answers) == 1:
      break

  total = answers[0]

  print(total[xr] + total[yr] + total[zr])

getIntersections2()

# class Hailstone:
#   def __init__(self, sx, sy, sz, vx, vy, vz):
#     self.sx, self.sy, self.sz = sx, sy, sz
#     self.vx, self.vy, self.vz = vx, vy, vz

#     self.a = vy
#     self.b = -vx
#     self.c = vy * sx - vx * sy

#   def __repr__(self):
#     return "Hailstone{" + f"a={self.a}, b={self.b}, c={self.c}" + "}"
  
# lines = open('input.txt').read().splitlines()
# hailstones = [Hailstone(*map(int, line.replace("@", ",").split(","))) for line in lines]

# print(hailstones)

# for i, h1 in enumerate(hailstones):
#   for j, h2 in enumerate(hailstones[:i]):
#     a1, b1, c1 = h1.a, h1.b, h1.c
#     a2, b2, c2 = h2.a, h2.b, h2.c

#     if a1 * b2 == b1 * a2:
#       continue
#     x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
#     y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
