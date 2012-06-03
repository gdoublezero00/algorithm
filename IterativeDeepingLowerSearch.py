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
move_piece = [None] * 32

distance = (
		(),
		(0,1,2,1,2,3,2,3,4,),
		(1,0,1,2,1,2,3,2,3,),
		(2,1,0,3,2,1,4,3,2,),
		(1,2,3,0,1,2,1,2,3,),
		(2,1,2,1,0,1,2,1,2,),
		(3,2,1,2,1,0,3,2,1,),
		(2,3,4,1,2,3,0,1,2,),
		(3,2,3,2,1,2,1,0,1,),
)

def get_distance(board):
	v = 0
	for x in xrange(9):
		p = board[x]
		if p == 0: continue
		v += distance[p][x]
	return v

def id_lower_search(limit, move, space, lower):
	if move == limit:
		if board == GOAL:
			global count
			count += 1
			print move_piece[1:]
	else:
		for x in adjacent[space]:
			p = board[x]
			if move_piece[move] == p: continue
			board[space] = p
			board[x] = 0
			move_piece[move + 1] = p
			new_lower = lower - distance[p][x] + distance[p][space]
			if new_lower + move <= limit:
				id_lower_search(limit, move + 1, x, new_lower)
			board[space] = 0
			board[x] = p


if __name__ == '__main__':
	global count
	count = 0
	s = time.clock()
	n = get_distance(board)
	for x in xrange(n, 32):
		print 'move ', x
		id_lower_search(x, 0, board.index(0), n)
		if count > 0: break
	e = time.clock()
	print "%.3f" % (e - s)
	
