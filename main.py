print 'CSE 5243 Associate Rule Analysis by Kun Liu & Zhe Dong'

#load data
import load
(Data,Label,cdim) = load.load()

for i in range(0,1):
	
	#split data
	Train_Data = []
	Train_Label = []
	for j in range(0,5):
		if j!=i:
			Train_Data += Data[j]
			Train_Label += Label[j]
	Test_Data = Data[i]
	Test_Label = Label[i]

	#convert data into apriori format
	F1 = open('train.txt', 'w')
	for j in range(0, len(Train_Data)):
		#print 'doc #' + str(j) + ' with ' + str(len(Train_Data[j])) + 'keywords'
		for k in range(0, len(Train_Data[j])):
			F1.write(str(Train_Data[j][k]) + ' ')
		F1.write(Train_Label[j] + '\n')

	#generate appearance.txt
	F2 = open('appearance.txt', 'w')
	F2.write('antecedent\n')
	Label_Set = set(Train_Label)
	for label in Label_Set:
		F2.write( label + ' consequent\n')

	#train

	#evaluate

