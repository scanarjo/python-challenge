charCounts = dict()

with open('input.txt') as file:
  for line in file:
    for char in line:
      try:
        count = charCounts[char]
        charCounts[char] = count + 1
      except:
        charCounts[char] = 1

filtered = filter(lambda item : item[1] == 1, charCounts.items())

keys = dict(filtered).keys()

print(''.join(keys))
