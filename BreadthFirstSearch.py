import Queue
	
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
GOAL = [1,2,3,4,5,6,7,8,0,]

SIZE = 181440

class State:
	def __init__(self, board, space, prev):
		self.board = board
		self.space = space
		self.prev = prev
	
def bf_search(start):
	q = Queue.Queue(SIZE)
	q.put(State(start, start.index(0), None))
	table = {}
	table[tuple(start)] = True
	while not q.empty():
		a = q.get()
		for x in adjacent[a.space]:
			b = a.board[:]
			b[a.space] = b[x]
			b[x] = 0
			key = tuple(b)
			if key in table: continue
			c = State(b, x, a)
			if b == GOAL:
				print print_answer(c)
				return
			q.put(c)
			table[key] = True

def print_answer(x):
	if x is not None:
		print_answer(x.prev)
		print x.board

if __name__ == '__main__':
	bf_search([8,6,7,2,5,4,3,0,1,])

