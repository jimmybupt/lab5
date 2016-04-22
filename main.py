print 'CSE 5243 Associate Rule Analysis by Kun Liu & Zhe Dong'

#load data
import load
(Data,Label,cdim) = load.load()

for i in range(0,5):
	
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
	F1 = open('train'+str(i), 'w')
	for j in range(0, len(Train_Data)):
		#print 'doc #' + str(j) + ' with ' + str(len(Train_Data[j])) + 'keywords'
		for k in range(0, len(Train_Data[j])):
			F1.write(str(Train_Data[j][k]) + ' ')
		F1.write(Train_Label[j] + '\n')

	#generate appearance.txt
	F2 = open('appearance'+str(i), 'w')
	F2.write('antecedent\n')
	Label_Set = set(Train_Label)
	for label in Label_Set:
		F2.write( label + ' consequent\n')

	#output test
	F3 = open('test'+str(i), 'w')
	for j in range(0, len(Test_Data)):
		for k in range(0, len(Test_Data[j])):
			F3.write(str(Test_Data[j][k]))
			if k != len(Test_Data[j])-1:
				F3.write(' ')
		F3.write('\n')

	#output label
	F4 = open('test_label'+str(i), 'w')
	for j in range(0, len(Test_Data)):
		F4.write(str(Test_Label[j])+'\n')

	#train
	#from subprocess import call
	#import os
	#os.system("./exe.sh")
	#os.system("./apriori -tr -s30 -c40 -Rappearance.txt train.txt -")
	#call(["./apriori", "-tr", "-s30", "-c40", "-Rappearance.txt", "train.txt", "-"])

	#evaluate

