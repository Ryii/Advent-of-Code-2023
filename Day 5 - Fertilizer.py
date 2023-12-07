def getLowestLocation():
  f = open("input.txt", "r")
  lines = f.read().splitlines()
  lines.append('')

  allMaps = []
  curMap = []

  for line in lines[2:]:
    if line.endswith("map:"):
      curMap = []
    elif line == '':
      allMaps.append(curMap.copy())
    else:
      curMap.append([int(number) for number in line.split()])

  seeds = [int(seed) for seed in lines[0].split()[1:]]
  minLocation = float('inf')

  for seed in seeds:
    for map in allMaps:
      for mapRange in map:
        if seed in range(mapRange[1], mapRange[1] + mapRange[2]):
          seed = mapRange[0] + (seed - mapRange[1])
          break

    minLocation = min(minLocation, seed)  

  return minLocation

# print(getLowestLocation())


def lowestLocationFromRanges():
  f = open("input.txt", "r")
  lines = f.read().splitlines()
  lines.append('')

  allMaps = []
  curMap = []

  for line in lines[2:]:
    if line.endswith("map:"):
      curMap = []
    elif line == '':
      allMaps.append(curMap.copy())
    else:
      curMap.append([int(number) for number in line.split()])

  allMaps.reverse()

  seeds = [int(seed) for seed in lines[0].split()[1:]]
  seedsRanges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

  seed = 0
  found = False

  while not found and seed < 100000000:
    seed += 1
    curVal = seed

    for map in allMaps:
      for mapRange in map:
        if curVal in range(mapRange[0], mapRange[0] + mapRange[2]):
          curVal = mapRange[1] + (curVal - mapRange[0])
          break

    # range checker

    for start, end in seedsRanges:
      if curVal in range(start, start + end):
        found = True
        break
    
  return seed

print(lowestLocationFromRanges())


# def lowestLocationFromRanges():
#   f = open("input.txt", "r")
#   lines = f.read().splitlines()
#   lines.append('')

#   allMaps = []
#   curMap = []

#   for line in lines[2:]:
#     if line.endswith("map:"):
#       curMap = []
#     elif line == '':
#       allMaps.append(curMap.copy())
#     else:
#       curMap.append([int(number) for number in line.split()])

#   seeds = [int(seed) for seed in lines[0].split()[1:]]
#   seedsRanges = zip(*(iter(seeds),) * 2)
#   minLocation = float('inf')

#   for start, length in seedsRanges:
#     for seed in range(start, start + length):
#       for map in allMaps:
#         for mapRange in map:
#           if seed in range(mapRange[1], mapRange[1] + mapRange[2]):
#             seed = mapRange[0] + (seed - mapRange[1])
#             break

#       minLocation = min(minLocation, seed)  

#   return minLocation

# print(lowestLocationFromRanges())