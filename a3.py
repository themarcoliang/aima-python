# a3.py
# Written by Marco Liang
# Jul 3, 2020
# A tic tac toe game played against a computer that uses stats from random playouts to pick its moves

from copy import deepcopy
from random import choice

# Function that displays a board (array of 9 numbers)
# empty : 0
# player : 1
# computer : 2
playouts = 10 #how many random playouts to try, higher number makes computer smarter

def display(board):
    print("-------------")
    for i in range(0,9):
        if i%3==0:
            if i!=0:
                print("\n", end="")
            print("|", end=" ")
        if board[i] == 1:
            print("O", end=" | ")
        elif board[i] == 2:
            print("X", end=" | ")
        else:
            print(" ", end=" | ")
    print("\n-------------")

# Function that checks whether the game is over, returns True or False and the winner (0 if tied)
def game_over(board):
    noMove = 0 #this counts the number of lines that has no moves (ex. having both X and O in a diagonal line)
    
    #check columns
    for i in range(3):
        column = [board[i],board[i+3],board[i+6]]
        if column == [1,1,1]: #player wins
            return True, 1
        elif column == [2,2,2]: #computer wins
            return True, 2
        elif 1 in column and 2 in column: #this column no longer winnable by either player since both are in it
            noMove += 1
    
    #check rows
    for i in [0,3,6]:
        row = [board[i], board[i+1],board[i+2]]
        if row == [1,1,1]:
            return True, 1
        elif row == [2,2,2]:
            return True, 2
        elif 1 in row and 2 in row: 
            noMove += 1

    #check diagonals
    for i in [2,4]:
        diagonal = [board[4-i],board[4],board[4+i]]
        if diagonal == [1,1,1]:
            return True, 1
        elif diagonal == [2,2,2]:
            return True, 2
        elif 1 in diagonal and 2 in diagonal: 
            noMove += 1
    
    if noMove == 8: #all moves are done
        return True, 0 #it's a tie
    else:
        return False, None

# This simulates the game based on random moves until it's over and returns the winner
def random_playout(board, whoseTurn):
    res = game_over(board) #check if game is over
    if res[0]: #game is over
        return res[1] #return winner(or 0 for tied)
    possibleMoves = [i for i, value in enumerate(board) if value == 0]
    move = choice(possibleMoves)
    board[move] = whoseTurn
    #switch turns
    if whoseTurn == 1:
        whoseTurn = 2
    else:
        whoseTurn = 1
    #recursively try the next step
    return random_playout(board, whoseTurn)

def play_a_new_game():
    board = [0] * 9
    print("This is a game of Tic Tac Toe!")
    print("You will be playing against Paul the Computer!")
    print("The game board will be displayed as so:")
    print("-------------\n| O | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |\n-------------")
    # display(board)
    print("Specify your position by inputting the number")
    print("Enter 1 if you would like to start first, or 2 to let Paul go first")
    next = int(input())
    if next != 1 and next != 2:
        print("Unexpected input, exiting..")
        return
    while True:
        if next == 1: #human
            print("Enter the next move (0-8):")
            nextMove = int(input())
            if(nextMove > 8 or nextMove < 0 or board[nextMove] != 0):
                print("Illegal space, try again")
                continue
            board[nextMove] = 1
        else: #computer
            possibleMoves = [i for i, value in enumerate(board) if value == 0] #empty spots
            scores = [0] * len(possibleMoves) #score keeping array
            for i in range(len(possibleMoves)):
                for _ in range(playouts):
                    board_copy = deepcopy(board)
                    board_copy[possibleMoves[i]] = 2 #computer makes a move
                    winner = random_playout(board_copy, 1) #random_playout plays rest of game
                    if winner == 2: #if the computer won
                        scores[i] += 1
                    elif winner == 1: #if the computer lost
                        scores[i] -= 1
            nextMove = scores.index(max(scores)) #find the move with largest number of wins - losses
            print("Computer makes a move ({})!".format(possibleMoves[nextMove]))
            # print("Possible moves: ", possibleMoves)
            # print("Scores: ", scores)
            board[possibleMoves[nextMove]] = 2 #make that move
        display(board)
        result = game_over(board)
        if(result[0]):
            #game is over
            print("Game is over!")
            if result[1] == 1:
                print("You've won!")
            elif result[1] == 2:
                print("You just lost to a computer!")
            else:
                print("The game is tied! No more moves possible")
            return
        #change turns
        if next == 1:
            next = 2
        else:
            next = 1

if __name__ == '__main__':
    play_a_new_game()

