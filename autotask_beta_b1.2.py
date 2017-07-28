import random;
print ('Input max number of tasks per sample:')
mTaskNumber = input()
print ('Input number of samples:')
samplesNumber = input()
codesfile = open('codes.csv')
taskfile = open('task.txt', 'w')
biomaterialFile = open('bm.txt')
counter = 1
counter2 = 0
data = []
biomaterialList = []

for lines in codesfile:
	data.append(lines)
for lines in biomaterialFile:
	biomaterialList.append(lines[:-1])
taskfile.write('GLOBAL TEST MULTIPLE TASKS\n')
for samples in range(int(samplesNumber)):
	biomaterial = 0
	taskNumber = random.randint(1, int(mTaskNumber))
	for i in range(taskNumber):
		taskrandom = random.randint(1, len(data))
		if str(biomaterial) in data[taskrandom-1]:
			taskfile.write('s'+ str(counter)+';'+str(data[taskrandom-1]))
			bmfind = str(data[taskrandom-1])
			for k in range(len(biomaterialList)):
				if biomaterialList[k] == bmfind[-4:-1]:
					biomaterial = str(biomaterialList[k])
		else:
			while str(biomaterial) not in data[taskrandom-1]:
				taskrandom = random.randint(1, len(data))
			taskfile.write('s'+ str(counter)+';'+str(data[taskrandom-1]))

	counter = counter + 1
taskfile.close
codesfile.close

