import random;                                  #подключаем библиотеку функций рандом
print ('Input max number of tasks per sample:')
mTaskNumber = input()                           #ввод числа назначений
print ('Input number of samples:')
samplesNumber = input()                         #ввод числа образцов 
codesfile = open('codes.csv')                   #открываем для чтения файл с кодами
taskfile = open('task.txt', 'w')                #открываем или создаем и открываем для перезаписи файл с результом работы
biomaterialFile = open('bm.txt')                #открываем для чтения файл с биоматериалами
counter = 1                                     #объявление некоторых переменных и списков
data = []
biomaterialList = []
for lines in codesfile:                         #читаем файл кодов и построчно записываем в список data
	data.append(lines)
for lines in biomaterialFile:                   #читаем файл биоматериалов и записываем построчно в список biomaterialList
	biomaterialList.append(lines[:-1])
taskfile.write('GLOBAL TEST MULTIPLE TASKS\n')  #делаем 1 строку результирующего файла заполненной чем-нибудь, чтобы не убирать галочку в testingtools
for samples in range(int(samplesNumber)):       #главный цикл. Повторяем все операции для введенного числа образцов
	biomaterial = '0'                            #сброс кода биоматериала при переходе к новому образцу
	taskNumber = random.randint(1, int(mTaskNumber)) #радномно задаем число назначений на образец
	for i in range(taskNumber):                 #пробегаем это рандомное число в цикле чтобы создать нужное число дублей этого образца
		taskrandom = random.randint(1, len(data)) #случайное число в диапазоне числа строк файла с кодами
		if biomaterial in data[taskrandom-1]: #условие позволяющее создать на образец только те назначения, которые имеют тот же код биоматериала, что и предидущее назначениее
			taskfile.write('s'+ str(counter)+';'+str(data[taskrandom-1])) #записываем строку в конечный файл в виде s1;code;041
			bmfind = str(data[taskrandom-1])    #буферная переменная
			for k in range(len(biomaterialList)): #цикл и условия для проверки какой именно биоматериал был в последней строке записанной в файл
				if biomaterialList[k] == bmfind[-4:-1]: #пробегаем по списку биоматериалов и если встречаем тот что был в записанной в файл строке - записываем его в переменную, с которой будем сравнивать рандомные назначения для следующих дублей образца
					biomaterial = str(biomaterialList[k])
		else:                                   # если биоматериал из случайно выбранной строки файла с кодами не совпадает с предыдущим биоматериалом для этого образца - рандомно перебирать строки пока не найдем такой же. Как найдем - записываем строку в файл
			while str(biomaterial) not in data[taskrandom-1]: 
				taskrandom = random.randint(1, len(data))
			taskfile.write('s'+ str(counter)+';'+str(data[taskrandom-1]))
	counter = counter + 1                       #переходим к следующему образцу и крутим цикл дальше
taskfile.close                                  #закрыыавем открытые файлы
codesfile.close
