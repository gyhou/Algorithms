#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps = ['rock', 'paper', 'scissors']  # The three options
    num_games = 3 ** n  # How many game will be played
    # Create list of lists with 0 place holders for each player
    games = [[0] * n for x in range(num_games)]
    dividers = [3 ** x for x in range(0, n + 1)]
    for i in range(0, len(games)):
        for j in range(1, len(games[0]) + 1):
            games[i][-j] = rps[(i // dividers[j - 1]) % 3]

    return games


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
