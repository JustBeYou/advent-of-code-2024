s = 0 

def is_good(line):
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

    return good and (asc or desc)


with open('input_2.txt') as f:
    for line in f:
        line = line.strip().split()
        line = map(int, line)
        line = list(line)

        if len(line) == 1 or is_good(line):
            s += 1
            continue

        for i in range(len(line)):
            copy_line = line[:i] + line[i+1:]
            if is_good(copy_line):
                s += 1
                break 

print(s)
