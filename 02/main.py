__author__ = "Chiara PR"
__version__ = "01.02"
__date__ = "2022-12-02"

# LOSS = 0
DRAW = 3
WIN = 6
SCORE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

opponent = {"Rock" : "A","Paper" : "B", "Scissors" :  "C"}
# player = {"X" : "loss", "Y" : "draw", "Z" : "win"}

f_in = "./input.txt"

with open(f_in, 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        # print(SCORE)
        o = line.split()[0]
        end = line.split()[1]

        # use 3.10 to optimize using switch/case
        if end == 'X': # LOSS
            # SCORE += LOSS (0)
            if o == opponent['Rock']:
                SCORE += SCISSORS
            elif o == opponent['Paper']:
                SCORE += ROCK
            else: # o == 'Scissors':
                SCORE += PAPER
        elif end == 'Y': # DRAW
            SCORE += DRAW
            if o == opponent['Rock']:
                SCORE += ROCK
            elif o == opponent['Paper']:
                SCORE += PAPER
            else: # o == 'Scissors':
                SCORE += SCISSORS
        elif end == 'Z': # WIN
            SCORE += WIN
            if o == opponent['Rock']:
                SCORE += PAPER
            elif o == opponent['Paper']:
                SCORE += SCISSORS
            else: # o == 'Scissors':
                SCORE += ROCK

print(SCORE)
