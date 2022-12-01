__author__ = "Chiara PR"
__version__ = "01.02"
__date__ = "2022-12-01"

cal = []
f_in = "./01/input.txt"

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
            cal.append(res)
            res = 0

cal.sort(reverse=True)

print(cal[0] + cal[1] + cal[2])
