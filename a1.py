# a1.py

from search import *
from random import shuffle
import time

def make_rand_8puzzle():
    initial = [i for i in range(9)]
    while True:
        shuffle(initial)
        puzzle = EightPuzzle(initial)
        if(puzzle.check_solvability(puzzle.initial)):
            puzzle.initial = tuple(initial)
            puzzle.state = puzzle.initial
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

#referencing code from search.py of aima-python code base
def astar_search_modified(problem, h=None, display=False):
    start_time = time.time()
    h = memoize(h or problem.h, 'h')
    result = best_first_graph_search_modified(problem, lambda n: n.path_cost + h(n), display)
    elapsed_time = time.time() - start_time
    print("elapsed time: {}s".format(elapsed_time))
    return result

def best_first_graph_search_modified(problem, f, display=False):
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    nodes_popped = 0
    while frontier:
        node = frontier.pop()
        nodes_popped = nodes_popped+1
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            print("nodes popped: {}".format(nodes_popped))
            print("length of solution: {}".format(node.f))
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None

def misplaced_tile(node):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    return sum(s != g for (s, g) in zip(node.state, goal))

def manhattan(node):
    goalRow = (2,0,0,0,1,1,1,2,2)
    goalCol = (2,0,1,2,0,1,2,0,1)
    return sum(abs(i/3 - goalRow[s]) + abs(i%3 - goalCol[s]) for i,s in enumerate(node.state))

def max_of_both(node):
    return max(misplaced_tile(node), manhattan(node))

for i in range(1,10):       
    print("Run {}".format(i))
    s = make_rand_8puzzle()
    display(s.state)
    print("Using misplaced tile heuristic")
    astar_search_modified(s, misplaced_tile, False)
    print("Using Manhattan distance heuristic")
    astar_search_modified(s, manhattan, False)
    print("Using max of misplaced tile and Manhattan distance heuristics")
    astar_search_modified(s, max_of_both, False)