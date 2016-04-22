class Rule:
	def __init__(self):
		label = ""
		keywords = []
		support = 0.0
		confidence = 0.0

def accuracy(True_Label, Predict_Label):
	count=0
	for i in range(0,len(True_Label)):
		if(Predict_Label(i)==True_Label(i)):
			count+=1
	accuracy=1.0*count/len(True_Label)
	return accuracy

for i in range(0,5):
	Rules = []
	F1 = open('rule'+str(i), 'r')
	for line in F1:
		L = line.split(' ')
		R = Rule()
		R.label = L[0]
		R.confidence = float(L[-1].strip('() ,\n'))
		R.support = float(L[-2].strip('() ,\n'))
		R.keywords = L[2:-2]
		Rules.append(R)
		print R.keywords
	
	F2 = open('test'+str(i), 'r')
	Predict_Label = []
	for line in F2:
		L = line.split(' ')
		K = set(L)
		max_conf = 0.0
		max_label = 'earn'
		for rule in Rules:
			match = True
			for word in rule.keywords:
				if word not in K:
					#print word + ' not in ',
					#print K
					match = False
					break
			if match:
				if rule.confidence > max_conf:
					max_conf = rule.confidence
					max_label = rule.label
		Predict_Label.append(max_label)

	F3 = open('test_label'+str(i), 'r')
	True_Label = []
	for line in F3:
		True_Label.append(line.strip(' \n'))

	print Predict_Label
	print True_Label
print accuracy(True_Label, Pridict_Label)
