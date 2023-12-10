def getExtrapolatedSum():
  f = open("input.txt", "r")
  lines = f.read().splitlines()

  total = 0

  for line in lines:
    values = [int(val) for val in line.split()]
    arr = [values.copy()]

    while any(values):
      values = [values[i] - values[i-1] for i in range(1, len(values))]
      arr.append(values.copy())

    for arrLine in arr:
      total += arrLine[-1]

  return total

# print(getExtrapolatedSum())

def getExtrapolatedSPrevSum():
  f = open("input.txt", "r")
  lines = f.read().splitlines()

  total = 0

  for line in lines:
    values = [int(val) for val in line.split()]
    arr = [values.copy()]

    while any(values):
      values = [values[i] - values[i-1] for i in range(1, len(values))]
      arr.append(values.copy())

    arr = arr[::-1]

    val = 0
    for arrLine in arr[1:]:
      val = arrLine[0] - val
    total += val

  return total

print(getExtrapolatedSPrevSum())