import Queue

adjacent = ((1,2,),
		    (0,2,3,),
			(0,1,4,),
			(1,4,5,),
			(2,3,6,),
			(3,),
			(1,))

q = Queue.Queue()

#
# depth first search
#
def df_search(goal, path):
	n = path[len(path) - 1]
	if n == goal:
		print path
	else:
		for x in adjacent[n]:
			if x not in path:
				path.append(x)
				df_search(goal, path)
				path.pop()

#
# breadth first search
#
def bf_search(start, goal):
	q.put(start)
	while q.qsize() > 0:
		path = q.get()
		n = path[len(path) - 1]
		if n == goal:
			print path
		else:
			for x in adjacent[n]:
				if x not in path:
					new_path = path[:]
					new_path.append(x)
					q.put(new_path)

def id_search(limit, goal, path):
	n = len(path)
	m = path[n - 1]
	if n == limit:
		if m == goal: print path
	else:
		for x in adjacent[m]:
			if x not in path:
				path.append(x)
				id_search(limit, goal, path)
				path.pop()
			
		

if __name__ == '__main__':
	print "--- depth first search ---"
	df_search(6, [0])
	print "--- breadth first search ---"
	bf_search([0], 6)

	print "--- iterative deeping ---"
	for x in range(1,8):
		print x, 'moves'
		id_search(x, 6, [0])

