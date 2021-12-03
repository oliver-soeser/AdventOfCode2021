# Day 1: Sonar Sweep - Part 2
f = open('input.txt', 'r')

sums = []

for i in f.readlines():
    i = int(i)
    if len(sums) > 0:
        sums[len(sums)-1] += i
    if len(sums) > 1:
        sums[len(sums)-2] += i
    sums.append(i)

prev = None
count = 0

for i in sums:
    i = int(i)
    if prev is not None:
        if i > prev:
            count += 1
    prev = i

print(count)
