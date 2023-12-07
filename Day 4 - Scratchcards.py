def getPoints():
  f = open("input.txt", "r")
  games = f.read().splitlines()

  total = 0

  for game in games:
    count = 0
    winningNums = set([word for word in game.split('|')[0].split()[2:]])
    myNums = set([word for word in game.split('|')[1].split()])
    
    for num in myNums:
      if num in winningNums:
        count = 1 if count == 0 else count * 2

    total += count

  return total

# print(getPoints())


def getScratchcards():
  f = open("input.txt", "r")
  games = f.read().splitlines()

  cards = [1] * len(games)

  for i, game in enumerate(games):
    matches = 0
    winningNums = set([word for word in game.split('|')[0].split()[2:]])
    myNums = set([word for word in game.split('|')[1].split()])
    
    for num in myNums:
      if num in winningNums:
        matches += 1

    for match in range(matches):
      cards[i + 1 + match] += cards[i]

  return sum(cards)

print(getScratchcards())