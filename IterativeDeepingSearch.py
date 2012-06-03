import time
	
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

board = [8,6,7,2,5,4,3,0,1,]
#board = [1,2,3,4,5,6,0,7,8,]

SIZE = 32
move_piece = [None] * SIZE


def id_search(limit, move, space):
	if move == limit:
		if board == GOAL:
			global count
			count += 1
#print move_piece[1:]
			print board
			printResult(move_piece)
	else:
		for x in adjacent[space]:
			p = board[x]
			if move_piece[move] == p: continue
			board[space] = p
			board[x] = 0
			move_piece[move + 1] = p
			id_search(limit, move + 1, x)
			board[space] = 0
			board[x] = p

def printResult(result):
	for x in result:
		if x != None:
			print x, ",",
	print ""


if __name__ == '__main__':
	global count
	count = 0
	s = time.clock()
	for x in xrange(1,SIZE):
		print 'move ', x
		id_search(x, 0, board.index(0))
		if count > 0: break
	e = time.clock()
	print "%.3f" % (e - s)
