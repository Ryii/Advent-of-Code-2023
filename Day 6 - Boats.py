def getRecords():
  f = open("input.txt", "r")
  lines = f.read().splitlines()

  times = [int(time) for time in lines[0].split()[1:]]
  distances = [int(distance) for distance in lines[1].split()[1:]]

  total = 1

  for (time, distance) in zip(times, distances):
    count = 0
    end = False   # optimization
    for i in range(time):
      if (time - i) * i > distance:
        count += 1
        if end == False:
          end = True
      elif end == True:
        break

    total *= count if count else 1

  return total

# print(getRecords())


def getKerningTimes():
  f = open("input.txt", "r")
  lines = f.read().splitlines()

  times = [time for time in lines[0].split()[1:]]
  distances = [distance for distance in lines[1].split()[1:]]

  totalTime = int(''.join(times))
  totalDistance = int(''.join(distances))
  print(totalTime)

  count = 0

  end = False   # optimization
  for i in range(totalTime):
    if (totalTime - i) * i > totalDistance:
      count += 1
      if end == False:
        end = True
    elif end == True:
      break

  return count

print(getKerningTimes())