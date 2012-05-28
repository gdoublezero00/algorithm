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

FORE = 1
BACK = 0

class State0:
	def __init__(self, board, space, prev, dirs):
		self.board = board
		self.space = space
		self.prev = prev
		self.dirs = dirs

def bi_search(start):
	q = Queue.Queue()
	table = {}
	a = State0(start, start.index(0), None, FORE)
	q.put(a)
	table[tuple(start)] = a
	a = State0(GOAL, GOAL.index(0), None, BACK)
	q.put(a)
	table[tuple(GOAL)] = a
	while not q.empty():
		a = q.get()
		for x in adjacent[a.space]:
			b = a.board[:]
			b[a.space] = b[x]
			b[x] = 0
			key = tuple(b)
			if key in table:
				c = table[key]
				if c.dirs != a.dirs:
					print_answer1(a, c)
					return
			else:
				c = State0(b, x, a, a.dirs)
				q.put(c)
				table[key] = c

def print_answer(x):
	if x is not None:
		print_answer(x.prev)
		print x.board

def print_answer1(a, b):
	if a.dirs == FORE:
		print_answer(a)
		print_answer_goal(b)
	else:
		print_answer(b)
		print_answer_goal(a)

def print_answer_goal(a):
	while a is not None:
		print a.board
		a = a.prev

if __name__ == '__main__':
	bi_search([8,6,7,2,5,4,3,0,1,])

	
