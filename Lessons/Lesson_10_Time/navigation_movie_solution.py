import time
import random

def create_board(size,x,y,treasure_x,treasure_y):
	board = []
	i = 0
	while i < size:
		board.append([' ']*(size))
		i += 1
	board[y][x]="0"
	board[treasure_y][treasure_x]="X"
	return board

def pretty_print(grid):
	for row in reversed(grid):
		print("".join(row))


size = 7
x = 0
y = 0
print("Try to make it to (5,4)\n")

playing = True
while playing:
	direction = random.choice(['a','s','d','w'])
	if (direction == 'a') and (x > 0):
		x -=1
	elif direction == 's' and (y > 0):
		y -=1
	elif direction == 'd' and (x < size-1):
		x +=1
	elif direction == 'w' and (y < size-1):
		y +=1
	if (x == 5) and (y == 4):
		print("You win!")
		playing = False
	pretty_print(create_board(size,x,y,5,4))
	time.sleep(0.01)
