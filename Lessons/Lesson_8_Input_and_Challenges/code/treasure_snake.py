from random import randint
from pynput import keyboard

def print_board(board,frame):
	print(frame*(len(board[0])+2))
	for row in board:
		print(frame + "".join(row) + frame)
	print(frame*(len(board[0])+2))

def mark(board,coordinates,symbol):
	board[coordinates[0]][coordinates[1]]=symbol

def place_treasure(board,body,treasure_symbol):
	treasure = body[0]
	size = len(board)
	if len(body) >= size*size:
		return
	while treasure in body:
		treasure = [randint(0,size-1),randint(0,size-1)]
	mark(board,treasure,treasure_symbol)
	return treasure

def valid_move(coordinates, direction, size):
	if direction == "a" and coordinates[1] > 0:
		coordinates[1]-=1
	elif direction == "d" and coordinates[1] < size-1:
		coordinates[1]+=1
	elif direction == "s" and coordinates[0] < size - 1:
		coordinates[0]+=1
	elif direction == "w" and coordinates[0] > 0:
		coordinates[0]-=1
	else:
		return False
	return True


def play(size=6,player="0",blank=" ",treasure_symbol="X",frame="#"):
	playing = True
	board = [[blank]*size for i in range(size)]
	body = [[randint(0,size-1),randint(0,size-1)]]
	treasure = place_treasure(board,body,treasure_symbol)

	print("Find the treasure! It is marked {}".format(treasure_symbol))

	while playing:
		head = body[0][:]
		tail = body.pop()
		mark(board,head,player)
		print_board(board,frame=frame)


		print("Enter a direction (asdw)")
		direction = input()

		if not valid_move(head,direction,size) or (head in body):
			playing = False
		body = [head] + body

		if head == treasure:
			body = body + [tail]
			treasure = place_treasure(board,body,treasure_symbol)
		else:
			mark(board,tail,blank)

	if len(body) == size*size:
		print("YOU WIN!")
	else:
		print("YOU LOSE!")


def play_continuous(size=6,player="0",blank=" ",treasure_symbol="X",frame="#"):
	class Game:
		board = [[blank]*size for i in range(size)]
		body = [[randint(0,size-1),randint(0,size-1)]]
		treasure = place_treasure(board,body,treasure_symbol)


	game = Game()
	mark(game.board,game.body[0],player)
	print_board(game.board,frame=frame)
	print("Find the treasure! It is marked {}".format(treasure_symbol))
	print("Enter a direction (asdw)")

	def on_press(key):
		try:
			k = key.char # single-char keys
		except:
			return False

		if k not in ['a', 's', 'd', 'w']: # keys interested
			print("KEY NOT IN SET")
			return False


		game.head = game.body[0][:]
		game.tail = game.body.pop()

		direction = k

		if not valid_move(game.head,direction,size) or (game.head in game.body):
			return False
		else:
			mark(game.board,game.head,player)

		game.body = [game.head] + game.body

		if game.head == game.treasure:
			game.body = game.body + [game.tail]
			game.treasure = place_treasure(game.board,game.body,treasure_symbol)
			if game.treasure is None:
				return False
		else:
			mark(game.board,game.tail,blank)
			mark(game.board,game.head,player)

		print_board(game.board,frame=frame)
		print("Enter a direction (asdw)")

	with keyboard.Listener(on_press=on_press) as lis:
		lis.join() # no this if main thread is polling self.keys


	if len(game.body) == size*size:
		print("YOU WIN!")
	else:
		print("YOU LOSE!")
	keyboard.Listener.stop


play_continuous() #must run sudo python treasure_snake.py
# play()
