
# hu
def display(board):
    print("  =   =   = ")
    for i in range(0,9):
        if i%3==0:
            if i!=0:
                print("\n", end="")
            print("|", end=" ")
        if board[i] == 0:
            print(" ", end=" | ")
        elif board[i] == 1:
            print("O", end=" | ")
        else:
            print("X", end=" | ")
    print("\n  =   =   = ")

display([0,0,0,0,1,1,1,1,2])