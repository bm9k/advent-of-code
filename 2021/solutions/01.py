with open("../inputs/01.txt", "r") as f:
  lines = [int(v) for v in f]

count = 0
for i in range(1, len(lines)):
  if lines[i] > lines[i - 1]:
    count += 1

# 1a
print(count)


count = 0
for i in range(3, len(lines)):
  if lines[i] > lines[i - 3]:
    count += 1

# 1b
print(count)