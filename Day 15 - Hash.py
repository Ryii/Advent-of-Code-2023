from collections import defaultdict

def sumHash():
  total = 0
  for hash in open("input.txt").read().split(","):
    sum = 0
    for c in hash:
      sum = ((sum + ord(c)) * 17) % 256

    total += sum
  print(total)


def sumHashFocus():
  total = 0

  # boxNumber : [(label, focal)]
  boxes = defaultdict(list)

  def calcHash(string):
    sum = 0
    for c in string:
      sum = ((sum + ord(c)) * 17) % 256
    return sum

  for hash in open("input.txt").read().split(","):
    if hash[-1] == "-":   # Case 1: "-" remove lens if in
      label = hash[:len(hash)-1]
      try:
        index = [pair[0] for pair in boxes[calcHash(label)]].index(label)
        boxes[calcHash(label)].pop(index)
      except:
        pass

    else:                 # Case 2: "="
      label, focal = hash.split('=')
      if label in [pair[0] for pair in boxes[calcHash(label)]]:
        index = [pair[0] for pair in boxes[calcHash(label)]].index(label)
        boxes[calcHash(label)][index] = (label, focal)
      else:
        boxes[calcHash(label)].append((label, focal))

  for i in range(256):
    for n, tup in enumerate(boxes[i], 1):
      total += (i + 1) * int(tup[1]) * n
      
    
  print(total)

sumHashFocus()