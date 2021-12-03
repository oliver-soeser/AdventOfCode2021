# Day 2: Dive! Part 2
f = open("input.txt", "r")

hPos = 0
depth = 0
aim = 0

for i in f.readlines():
    j = i.split(" ")
    command = j[0]
    amount = int(j[1])

    if command == "forward":
        hPos += amount
        depth += aim*amount
    elif command == "up":
        aim -= amount
    elif command == "down":
        aim += amount

print(hPos*depth)
