__author__ = "Chiara PR"
__version__ = "01.01"
__date__ = "2022-12-03"

f_in = "./input.txt"


def priority(ch):
    p = ord(ch)
    if p < 97:
        p = (p - 65) + 27
    else:
        p = (p - 97) + 1
    return p


with open(f_in, 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f]
 
    p = []
    for line in lines:
        l = len(line) // 2
        d = ''.join(set(line[:l]).intersection(set(line[l:])))
        p.append(priority(d[0]))

print(sum(p))

            

