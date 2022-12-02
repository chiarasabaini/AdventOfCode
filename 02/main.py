__author__ = "Chiara PR"
__version__ = "01.01"
__date__ = "2022-12-02"

# LOSS = 0
DRAW = 3
WIN = 6
SCORE = 0

# opponent = {"A" : "Rock", "B" : "Paper", "C" : "Scissors"}
# player = {"X" : 1, "Y" : 2, "Z" : 3}

f_in = "./input.txt"

with open(f_in, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

    for line in lines:
        # print(SCORE)
        o = line.split()[0]
        p = line.split()[1]

        if p == 'X':
            SCORE += 1
            if o == 'A':
                SCORE += DRAW
            elif o == 'C':
                SCORE += WIN
        elif p == 'Y':
            SCORE += 2
            if o == 'B':
                SCORE += DRAW
            elif o == 'A':
                SCORE += WIN
        elif p == 'Z':
            SCORE += 3
            if o == 'C':
                SCORE += DRAW
            elif o == 'B':
                SCORE += WIN


print(SCORE)
