import math
from collections import deque

class Module:
  def __init__(self, name,type, outputs):
    self.name = name
    self.type = type
    self.outputs = outputs

    if type == "%":
      self.memory = "off"
    else:
      self.memory = {}

  def __repr__(self):
    return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

modules = {}
targets = []

for line in open("input.txt").read().splitlines():
  l, r = line.strip().split(" -> ")
  outputs = r.split(", ")
  if l == "broadcaster":
    targets = outputs
  else:
    type = l[0]
    name = l[1:]
    modules[name] = Module(name, type, outputs)

for name, module in modules.items():
  for output in module.outputs:
    if output in modules and modules[output].type == "&":
      modules[output].memory[name] = "lo"

(feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

presses = 0

while True:
  presses += 1
  q = deque([("broadcaster", target, "lo") for target in targets])

  while q:
    origin, target, pulse = q.popleft()
    if target not in modules:
      continue
    module = modules[target]

    if module.name == feed and pulse == "hi":
      seen[origin] += 1

      if origin not in cycle_lengths:
        cycle_lengths[origin] = presses
      else:
        assert presses == seen[origin] * cycle_lengths[origin]

      if all(seen.values()):
        n = 1
        for cycle_length in cycle_lengths.values():
          n = math.lcm(n, cycle_length)
        print(n)
        exit(0)

    if module.type == "%":
      if pulse == "lo":
        module.memory = "on" if module.memory == "off" else "off"
        outgoing = "hi" if module.memory == "on" else "lo"
        for output in module.outputs:
          q.append(((module.name, output, outgoing)))
    else:
      module.memory[origin] = pulse
      outgoing = "lo" if all(module == "hi" for module in module.memory.values()) else "hi"
      for output in module.outputs:
        q.append((module.name, output, outgoing))
