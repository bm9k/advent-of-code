with open("../inputs/01.txt", "r") as f:
  elves = f.read().split("\n\n")

result = []

for elf in elves:
  calories = (int(x) for x in elf.split())
  result.append(sum(calories))

# 1a
print(max(result))

# 1b
result = sorted(result)
print(sum(result[-3:]))