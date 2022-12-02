with open("../inputs/02.txt", "r") as f:
  lines = f.read().split("\n")

depth = 0
horizontal = 0

for line in lines:
  direction, value = line.split()
  value = int(value)

  if direction == "forward":
    horizontal += value
  elif direction == "down":
    depth += value
  else:
    depth -= value

# 02a
print(depth * horizontal)


depth = 0
horizontal = 0
aim = 0

for line in lines:
  direction, value = line.split()
  value = int(value)

  if direction == "forward":
    horizontal += value
    depth += aim * value
  elif direction == "down":
    aim += value
  else:
    aim -= value

# 02b
print(depth * horizontal)
