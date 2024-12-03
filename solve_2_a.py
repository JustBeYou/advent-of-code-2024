s = 0 

with open('input_2.txt') as f:
    for line in f:
        line = line.strip().split()
        line = map(int, line)
        line = list(line)

        if len(line) == 1:
            s += 1
            continue

        asc = True
        desc = True
        good = True

        for i in range(len(line) - 1):
            if line[i] <= line[i + 1]:
                desc = False

            if line[i] >= line[i + 1]:
                asc = False

            d = abs(line[i] - line[i + 1])
            if d < 1 or d > 3:
                good = False

        if good and (asc or desc):
            s += 1

print(s)
