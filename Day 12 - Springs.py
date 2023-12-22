def getSumSprings():
  lines = open("input.txt").read().splitlines()

  def getCount(springs, nums):
    if springs == "":
      return 1 if nums == () else 0
    if nums == ():
      return 0 if "#" in springs else 1

    result = 0

    if springs[0] in ".?":
      result += getCount(springs[1:], nums)
    
    if springs[0] in "#?":
      if nums[0] <= len(springs) and "." not in springs[:nums[0]] and (nums[0] == len(springs) or springs[nums[0]] != "#"):
        result += getCount(springs[nums[0] + 1:], nums[1:])

    return result

  total = 0

  for line in lines:
    springs, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    total += getCount(springs, nums)

  return total

# print(getSumSprings())


def getSumSpringsUnfolded():
  lines = open("input.txt").read().splitlines()

  cache = {}

  def getCount(springs, nums):
    if springs == "":
      return 1 if nums == () else 0
    if nums == ():
      return 0 if "#" in springs else 1
    
    key = (springs, nums)

    if key in cache:
      return cache[key]

    result = 0

    if springs[0] in ".?":
      result += getCount(springs[1:], nums)
    
    if springs[0] in "#?":
      if nums[0] <= len(springs) and "." not in springs[:nums[0]] and (nums[0] == len(springs) or springs[nums[0]] != "#"):
        result += getCount(springs[nums[0] + 1:], nums[1:])

    cache[key] = result

    return result

  total = 0

  for line in lines:
    springs, nums = line.split()
    nums = tuple(map(int, nums.split(",")))

    springs = "?".join([springs] * 5)
    nums *= 5

    total += getCount(springs, nums)

  return total

print(getSumSpringsUnfolded())
