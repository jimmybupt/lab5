def load():

	vector_file = open('vector1.txt', 'r')
	label_file = open('label.txt', 'r')

	import ast
	import sys
	import time
	info = open("info.txt",'r') #stores the number of vectors and length of vectors
	rdim = int(info.readline())
	cdim = int(info.readline())

	DIC = []
	vocabulary = open("vocabulary.txt", 'r')
	for word in vocabulary:
		DIC.append(str(word).rstrip())

	cross_fold = 5 #number of blocks for cross validation
	block_size = rdim / cross_fold
	S = []	#vectors
	L = []	#labels

	for i in range(0, cross_fold):
		size = block_size
		if i == cross_fold - 1:
			size = rdim - ((cross_fold-1)*block_size)
		M = []
		for j in range(0, size):
			M.append([])
		V = [None] * size
		S.append(M)
		L.append(V)

	initial_time = time.time()

	print "Reading vectors... ",
	sys.stdout.flush()
	i = 0
	for line in vector_file:
		#print 'read doc #' + str(i)
		block = i / block_size
		if block >= cross_fold:
			block = cross_fold - 1
		offset = i - block_size * block

		data = ast.literal_eval(line)
		for D in data:
			#print 'find word ' + DIC[int(D[0])]
			S[block][offset].append(DIC[int(D[0])])
		#print str(len(S[block][offset])) + ' ' + str(block) + ' ' + str(offset)
		i=i+1
		if i==rdim:
			break

	i = 0
	for line in label_file:
		block = i / block_size
		if block >= cross_fold:
			block = cross_fold - 1
		offset = i - block_size * block

		label = ast.literal_eval(line)
		L[block][offset] = str(label[0])
		i = i+1
		if i==rdim:
			break

	print "done"

	return (S, L, cdim)
