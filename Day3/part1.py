# Day 3: Binary Diagnostic - Part 1
f = open("input.txt", "r")

temp1 = []
temp2 = []
gamma = []
epsilon = []

for i in f.readlines():
    temp1.append([])
    for j in i:
        temp1[len(temp1)-1].append(j)

for i in range(len(temp1[0])):
    if i == len(temp1[0])-1:
        # Don't include the newline character
        break

    temp2.append(0)
    for j in range(len(temp1)):
        temp2[i] += int(temp1[j][i])

for i in temp2:
    if i < len(temp1)/2:
        gamma.append(0)
    else:
        gamma.append(1)

for i in gamma:
    if i == 0:
        epsilon.append(1)
    else:
        epsilon.append(0)

print(int("".join(str(i) for i in gamma), 2) *
      int("".join(str(i) for i in epsilon), 2))
