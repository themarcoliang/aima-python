# a1.py

from search import *
from random import shuffle

def make_rand_8puzzle():
    initial = [i for i in range(9)]
    while True:
        shuffle(initial)
        puzzle = EightPuzzle(initial)
        if(puzzle.check_solvability(puzzle.initial)):
            break
    return puzzle

def display(state):
    for i in range(len(state)):
        if(state[i]==0):
            print('*', end=' ')
        else:
            print(state[i], end=' ')
        if((i+1)%3==0):
            print('\n', end='')

s = make_rand_8puzzle()
display(s.initial)