import time

class Rule:
	def __init__(self):
		label = ""
		keywords = []
		support = 0.0
		confidence = 0.0

def accuracy(True_Label, Predict_Label):
	count=0
	for i in range(0,len(True_Label)):
		if(Predict_Label[i]==True_Label[i]):
			count+=1
	accuracy=1.0*count/len(True_Label)
	return accuracy

cross_fold = 5 #number of blocks for cross validation
total_time=0
accuracy_list=[]
count=0
for i in range(0,cross_fold):
  	print ("") 
  	print ("cross validation trial: "+str(i+1)+" out of "+str(cross_fold))
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
		#print R.keywords
	
	F2 = open('test'+str(i), 'r')
	start_time=time.time()
	Predict_Label = []
	for line in F2:
		count+=1
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
	single_time=time.time()-start_time
	total_time+=single_time
	F3 = open('test_label'+str(i), 'r')
	True_Label = []
	for line in F3:
		True_Label.append(line.strip(' \n'))

	#print Predict_Label
	#print True_Label
	acc=accuracy(True_Label, Predict_Label) 
	accuracy_list.append(acc) 
	print ("  accuracy is: " +  str(acc))
print ("average online cost for classification is: " +str(total_time/count))
print ("average accuracy for classification is: " +str(sum(accuracy_list)/cross_fold))
