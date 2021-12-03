# Day 2: Dive! Part 1
f = open("input.txt", "r")

hPos = 0
depth = 0

for i in f.readlines():
    j = i.split(" ")
    command = j[0]
    amount = int(j[1])

    if command == "forward":
        hPos += amount
    elif command == "up":
        depth -= amount
    elif command == "down":
        depth += amount

print(hPos*depth)
