def getWinnings():

  # with open("input2.txt") as file:
  #   hands = file.read().splitlines()

  f = open("input.txt", "r")
  hands = f.read().splitlines()

  labelsMap = {"1": 1, "2": 2, "3": 3,  "4": 4,  "5": 5,  "6": 6,  "7": 7, 
               "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
  
  values = [0] * len(hands)

  #   type 1: 5 of a kind;  type 2: 4 of a kind;   type 3: Full house;   type 4: Three of a kind;
  #   type 5: Two pair;     type 6: One pair;      type 7: High card;

  for i, hand in enumerate(hands):
    cards, bid = hand.split()[0], int(hand.split()[1])

    scores = [labelsMap[i] for i in cards]
    scoresDict = {x: scores.count(x) for x in scores}
    typeArray = sorted(scoresDict.values(), reverse=True)

    # types
    if typeArray == [5]:
      type = 1
    elif typeArray == [4, 1]:
      type = 2
    elif typeArray == [3, 2]:
      type = 3
    elif typeArray == [3, 1, 1]:
      type = 4
    elif typeArray == [2, 2, 1]:
      type = 5
    elif typeArray == [2, 1, 1, 1]:
      type = 6
    else:
      type = 7

    values[i] = (type, scores, bid)

  values = sorted(values, key=lambda x:(x[0], [-n for n in x[1]]), reverse=True)
  total = 0

  for i, value in enumerate(values, 1):
    print(i, value)
    total += value[2] * i

  return total

# print(getWinnings())


def getWinnings():

  f = open("input.txt", "r")
  hands = f.read().splitlines()

  labelsMap = {"1": 1, "2": 2, "3": 3,  "4": 4, "5": 5,  "6": 6,  "7": 7, 
               "8": 8, "9": 9, "T": 10, "J": 0, "Q": 12, "K": 13, "A": 14}
  
  values = [0] * len(hands)

  #   type 1: 5 of a kind;  type 2: 4 of a kind;   type 3: Full house;   type 4: Three of a kind;
  #   type 5: Two pair;     type 6: One pair;      type 7: High card;

  for i, hand in enumerate(hands):
    cards, bid = hand.split()[0], int(hand.split()[1])

    jokers = cards.count("J")

    scores = [labelsMap[i] for i in cards if i != "J"]
    scoresDict = {x: scores.count(x) for x in scores}
    typeArray = sorted(scoresDict.values(), reverse=True)

    if len(typeArray) > 0:
      typeArray[0] += jokers
    else:
      typeArray = [5]

    # types
    if typeArray == [5]:
      type = 1
    elif typeArray == [4, 1]:
      type = 2
    elif typeArray == [3, 2]:
      type = 3
    elif typeArray == [3, 1, 1]:
      type = 4
    elif typeArray == [2, 2, 1]:
      type = 5
    elif typeArray == [2, 1, 1, 1]:
      type = 6
    else:
      type = 7

    scores = [labelsMap[i] for i in cards]
    values[i] = (type, scores, bid)

  values = sorted(values, key=lambda x:(x[0], [-n for n in x[1]]), reverse=True)
  total = 0

  for i, value in enumerate(values, 1):
    print(i, value)
    total += value[2] * i

  return total

print(getWinnings())