# Day 1: Sonar Sweep - Part 1
f = open('input.txt', 'r')

prev = None
count = 0

for i in f.readlines():
    i = int(i)
    if prev is not None:
        if i > prev:
            count += 1
    prev = i

print(count)
