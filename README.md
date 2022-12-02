# Advent of Code

![Tags](https://badgen.net/badge/icon/%23AdventOfCode%20%23python/14406F1?icon=https://icons.getbootstrap.com/assets/icons/bookmarks-fill.svg&label&labelColor=FFF) ![Author](https://badgen.net/badge/Author/Chiara%20PR/60C?labelColor=000) ![Version](https://badgen.net/badge/Version/01.02/cyan?labelColor=000)
---

# Table of Contents

- [Advent of Code](#advent-of-code)
- [Table of Contents](#table-of-contents)
    - [Description](#description)
    - [Daily Challenges](#daily-challenges)
    - [Requirements](#requirements)
    - [Directories structure](#directories-structure)
    - [Useful Links](#useful-links)

---

## Description

[Advent of Code](https://adventofcode.com/2022/about) is an Advent calendar of *small programming puzzles* for a variety of skill sets and skill levels that can be solved in *any programming language you like*. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to *challenge each other*.

---

## Daily Challenges

### Day 01

<details>
<summary>Part 1</summary>

    The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying.

    In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories.

    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
</details>

<details>
<summary>Part 2</summary>

    By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

    To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
</details>


### Day 02

<details>
<summary>Part 1</summary>

    The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

    Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

    Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

    The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

    The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    What would your total score be if everything goes exactly according to your strategy guide?
</details>

<details>
<summary>Part 2</summary>

    The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

    The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated.

    Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
</details>

---

## Requirements

-  ![Language](https://badgen.net/badge/Python/v3.9+/FFD343?labelColor=3776AB&icon=pypi) <sup>([Download](https://www.python.org/downloads/)) <small>[it has to be in the PATH]</small></sup>

---

## Directories structure

- ![AoC](https://badgen.net/badge/icon/AoC/E01B22?labelColor=FFF&icon=https://icons.getbootstrap.com/assets/icons/folder.svg&label)

    - ![01](https://badgen.net/badge/icon/01/000?labelColor=00FF00&icon=https://icons.getbootstrap.com/assets/icons/folder.svg&label)

        - [input.txt](./01/input.txt)
        - [main.py](./01/main.py)
    
    - ![02](https://badgen.net/badge/icon/02/000?labelColor=00FF00&icon=https://icons.getbootstrap.com/assets/icons/folder.svg&label)

        - [input.txt](./02/input.txt)
        - [main.py](./02/main.py)

    - ![docs](https://badgen.net/badge/icon/docs/000?labelColor=0CC8FF&icon=https://icons.getbootstrap.com/assets/icons/files.svg&label)

        - [CHANGELOG.txt](./docs/CHANGELOG.txt)

    - README.md

---

### Useful Links

[![AoC](https://badgen.net/badge/icon/Advent%20of%20Code/0052CC?icon=https://icons.getbootstrap.com/assets/icons/calendar2-heart.svg&label&labelColor=FFF)](https://adventofcode.com/)

---

Made with ♡ by [![Chiara PR](https://badgen.net/badge/icon/Chiara%20PR/B67DFF?icon=github&label&labelColor=000)](https://github.com/chiarasabaini)
