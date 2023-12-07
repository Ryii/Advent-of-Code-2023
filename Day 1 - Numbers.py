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

def sumCalibrationValues2():
  total = 0
  hashMap = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
             "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
  reversedHashMap = {"eno":1, "owt":2, "eerht":3, "ruof":4, "evif":5, "xis":6, "neves":7, "thgie":8, "enin":9,
             "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}

  f = open("input.txt", "r")
  Lines = f.readlines()
  
  for line in Lines:
    end = False
    i = 0

    while not end and i < len(line):
      if line[i:].startswith(tuple(hashMap.keys())):
        for key, value in hashMap.items():
          if line[i:].startswith(key):
            total += 10 * value
            end = True
            break
      i += 1

    line = line[::-1]
    end = False
    i = 0

    while not end and i < len(line):
      if line[i:].startswith(tuple(reversedHashMap.keys())):
        for key, value in reversedHashMap.items():
          if line[i:].startswith(key):
            total += value
            end = True
            break
      i += 1

  return total


print(sumCalibrationValues2())