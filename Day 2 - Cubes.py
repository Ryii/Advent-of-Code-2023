def getGameIDs():
  total = 0

  f = open("input.txt", "r")
  Lines = f.readlines()

  for line in Lines:
    id = int(line.split()[1][:-1])    # removes the colon from game ID
    tosses = [game.strip().replace(", ", ",") for game in line.split(":")[1].split(";")]
    
    red, blue, green = 0, 0, 0
    success = True

    for toss in tosses:
      cubes = toss.split(",")

      for cube in cubes:
        count, color = int(cube.split()[0]), cube.split()[1]
        if color == "red":
          red = count
        elif color == "blue":
          blue = count
        elif color == "green":
          green = count
      
      if red > 12 or blue > 14 or green > 13:
        success = False
        break

    total += id if success else 0

  return total


def getPowers():
  total = 0

  f = open("input.txt", "r")
  Lines = f.readlines()

  for line in Lines:
    tosses = [game.strip().replace(", ", ",") for game in line.split(":")[1].split(";")]
    
    red, blue, green = 0, 0, 0

    for toss in tosses:
      cubes = toss.split(",")

      for cube in cubes:
        count, color = int(cube.split()[0]), cube.split()[1]
        if color == "red":
          red = max(red, count)
        elif color == "blue":
          blue = max(blue, count)
        elif color == "green":
          green = max(green, count)

    total += red * blue * green

  return total



print(getPowers())