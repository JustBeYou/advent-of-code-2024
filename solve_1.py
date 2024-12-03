a = []
b = []

with open("input_1.txt") as f:
    for line in f:
        line = line.strip()
        x, y = line.split()
        a.append(int(x))
        b.append(int(y))

a.sort()
b.sort()

# part 1
d = 0
for x, y in zip(a, b):
    d += abs(x-y)

print(d)

# part 2

a = set(a)
s = 0

for y in b:
    if y in a:
        s += y

print(s)