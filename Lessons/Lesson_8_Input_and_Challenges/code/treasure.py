import random

size = 15
player = "Y"
blank = " "
treasure_symbol = "H"

def print_board(board):
    for row in board:
        print(row)

def move(coordinates, direction, size):
    if direction == "a" and coordinates[1] >0:
        coordinates[1]-=1
    elif direction == "d" and coordinates[1] < size-1:
        coordinates[1]+=1
    elif direction == "s" and coordinates[0] < size - 1:
        coordinates[0]+=1
    elif direction == "w" and coordinates[0] > 0:
        coordinates[0]-=1

def play():
    playing = True
    coordinates = [0,0]
    board = [[blank]*size for i in range(size)]
    board[random.randint(0,size-1)][random.randint(0,size-1)]=treasure_symbol
    print("Find the treasure! It is marked {}".format(treasure_symbol))
    while playing:
        board[coordinates[0]][coordinates[1]]=player
        print_board(board)
        board[coordinates[0]][coordinates[1]]=blank
        print("Enter a direction (asdw)")
        direction = input()
        move(coordinates,direction,size)
        if board[coordinates[0]][coordinates[1]] == treasure_symbol:
            print_board(board)
            print("You win!\n")
            playing = False



if __name__=="__main__":
    while True:
        play()
