

adjacent = (
		(1,3,),
		(0,2,4,),
		(1,5,),
		(0,4,6,),
		(1,3,5,7,),
		(2,4,8,),
		(3,7,),
		(4,6,8,),
		(5,7,),
)

GOAL = [1,2,3,4,5,6,7,8,0]
SIZE =181440

class State00:
	def __init__(self, board, space, prev, move):
		self.board = board
		self.space = space
		self.prev = prev
		self.move = move

def search_longest_move():
	buff = [None] * SIZE
	a = State00(GOAL, GOAL.index(0), None, 0)
	buff[0] = a
	front = 0
	rear = 1
	table = {}
	table[tuple(GOAL)] = a
	while front < rear:
		a = buff[front]
		for x in adjacent[a.space]:
			b = a.board[:]
			b[a.space] = b[x]
			b[x] = 0
			key = tuple(b)
			if key in table: continue
			c = State00(b, x, a, a.move + 1)
			buff[rear] = c
			rear += 1
			table[key] = c
		front += 1

	n = SIZE - 1
	move = buff[n].move
	print 'move = ', move
	while buff[n].move == move:
		print buff[n].board
		n -= 1

if __name__ == '__main__':
	search_longest_move()
