from random import randint
from pynput import keyboard


class Runner:

	def __init__(self,blank=" ",player="0",wall="_",w = 12,h = 12,wall_size=2):
		self.position = w//2
		self.blank = blank
		self.player = player
		self.wall = wall
		self.w = w
		self.h = h
		self.wall_size=wall_size

		self.board = [[blank]*w] + [self.one_row() for i in range(h-1)]
		self.board[0][self.position] = player

	def one_row(self):
		wall_start = randint(0,self.w-self.wall_size)
		return [self.blank]*wall_start + [self.wall]*self.wall_size + [self.blank]*(self.w-self.wall_size-wall_start)

	def print_board(self):
		for row in self.board[::-1]:
			print("#" + "".join(row) + "#")


	def valid_move(self,direction):
		if direction == "a" and self.position > 0:
			self.position-=1
		elif direction == "d" and self.position < len(self.board[0])-1:
			self.position+=1
		elif direction == "s" or direction == "w" or direction == "":
			pass
		else:
			return False

		return True


	def play(self):
		playing = True

		print("Avoid the walls!")

		while playing:


			self.print_board()


			print("Enter a direction: a, s, w, d, or nothing")
			direction = input()

			if not self.valid_move(direction) or (self.board[1][self.position]==self.wall):
				playing = False
			else:
				self.board.pop(0)
				self.board[0][self.position]=self.player
				self.board += [self.one_row()]

		print("YOU LOSE!")

	def play_continuous(self):
		print("Avoid the walls!")
		self.print_board()
		print("Enter a direction: a, s, w, d, or nothing")

		def one_move(key):
			try:
				direction = key.char # single-char keys
			except:
				return True
			if direction not in ['a', 's', 'd', 'w']: # keys interested
				return True
			if not self.valid_move(direction) or (self.board[1][self.position]==self.wall):
				return False
			else:
				self.board.pop(0)
				self.board[0][self.position]=self.player
				self.board += [self.one_row()]

			self.print_board()
			print("Enter a direction: a, s, w, d, or nothing")

		with keyboard.Listener(on_press=one_move) as lis:
			lis.join() # no this if main thread is polling self.keys

		print("YOU LOSE!")



r=Runner() #must run sudo python treasure_snake.py
r.play()
r.play_continuous()
