__author__ = "Chiara PR"
__version__ = "01.01"
__date__ = "2022-12-01"

elves = []
f_in = "input.txt"

with open(f_in, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # print(lines)

    res = 0
    for line in lines:
        if line != '\n':
            n = int(line.split('\n')[0])
            res += n
            # print(n)
            # print(res)
        else:
            elves.append(res)
            res = 0

print(max(elves))
