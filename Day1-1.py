def sumCalibrationValues():
  total = 0
  hashSet = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

  f = open("input.txt", "r")
  Lines = f.readlines()
  
  for line in Lines:
    for c in line:
      if c in hashSet:
        total += 10 * int(c)
        break

    for c in reversed(line):
      if c in hashSet:
        total += int(c)
        break

  return total


print(sumCalibrationValues())