#this program uses decision tree to predict moves for an x's and o's game
import random #to train the model, it will be able to play against randomly generated moves or the player herself
import numpy as np
from sklearn import tree
def printBoard(boardList): # this is just a method that takes the list which is the x and o grid and prints it
	for n in range(0,8,3):
		print("   ",end = "")
		print(boardList[n], end = "  |  ")
		print(boardList[n+1], end = "  |  ")
		print(boardList[n+2])
		if n != 6:
			print("--------------------") #just for visuals
			
def pvp(): #this is a player vs player module that will be a base for the game and its testing
	n = 0
	boardList = [0,1,2,3,4,5,6,7,8]
	learnList = [[],[],[],[]]
	#printBoard(boardList)
	newMoveList = []
	gameOn = True
	while gameOn == True:
		if n == 4:
			break
		move = random.randint(0,9)
		while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
			move = random.randint(0,9)
		boardList[move] = 'x'
		learnList[n].append(move)
		#printBoard(boardList)
		gameOn = checkwin(boardList)
		if gameOn == False:
			break
		move = random.randint(0,9)
		while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
			move = random.randint(0,9)
		boardList[move] = 'o'
		learnList[n].append(move)
		#printBoard(boardList)
		gameOn = checkwin(boardList)
		n+=1
	if whoWin(boardList) == 'o':
		return learnList
	else:
		return 'x'
def extractMove(boardList, newMoveList):
	for i in range(0,len(boardList)):
		if boardList[i]!= newMoveList[i]:
			return i

def whoWin(boardList):
	for n in range(0,7,3):
		if boardList[n] == boardList[n+1] and boardList[n] == boardList[n+2]:
			#print("the winner is... " + boardList[n] )
			#printBoard(boardList)
			if boardList[n]=='o' or boardList[n]!='x':
				return 'o'
	for n in range(0,3):
		if boardList[n]== boardList[n+3] and boardList[n]== boardList[n+6]:
			#print("the winner is... " + boardList[n] )
			#printBoard(boardList)
			if boardList[n]=='o' or boardList[n]!='x':
				return 'o'
	if (boardList[2] == boardList[4] and boardList[4]== boardList[6])or(boardList[0] == boardList[4] and boardList[4]== boardList[8]):
		#print("the winner is... " + boardList[4] )
		#printBoard(boardList)
		if boardList[4]=='o' or boardList[4]!='x':
				return 'o'
	return 'x'
def checkwin(boardList):
	for n in range(0,7,3):
		if boardList[n] == boardList[n+1] and boardList[n+1] == boardList[n+2]:
			return False
	for n in range(0,3):
		if boardList[n]== boardList[n+3] and boardList[n+3] == boardList[n+6]:
			return False
	if (boardList[2] == boardList[4] and boardList[2]== boardList[6]) or (boardList[0] == boardList[4] and boardList[0]== boardList[8]):
		return False
		
	else:
		return True

def randomMove(boardList,player): #in this case the player makes a random move
	#print("the other player makes a random move")
	move = random.randint(0,9)
	while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
		move = random.randint(0,9)
	boardList[move] = player
	return boardList

#the program starts here

finalList = [] #this final list is essentially a list of lists that we will take apart at feed to the decision tree algorithm 
numberO = 0
for i in range(0,200000): #this is the number of times you want to train the player with random numbers
	finalList.append(pvp())
	if finalList[-1]== 'x':
		finalList.pop()
print(finalList)
ffm = [] #features for the first move
fsm = [] #second move, third move...
ftm = [] 
ffom = []
lfm = [] #labels for the first, second, third and fourth moves
lsm = []
ltm = []
lfom = []
for i in finalList:
	ffm.append(i[0][0])
	lfm.append(i[0][1])
	prep1 = i[0] + i[1]
	if len(prep1) == 4:
		prep1.pop(3)
	fsm.append(prep1)
	lsm.append(i[1][1])
	prep2 = i[0]+i[1]+i[2]
	if len(prep2) == 6:
		prep2.pop(5)
	ftm.append(prep2)
	ltm.append(i[2][1])
	if len(i[3])==2:
		prep3 = i[0]+i[1]+i[2]+i[3]
		if len(prep3) == 8:
			prep3.pop(7)
		ffom.append(prep3)
		lfom.append(i[3][1])
print
clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(np.reshape(ffm,(-1,1)),np.reshape(lfm,(-1,1)))
clf2 = tree.DecisionTreeClassifier()
clf2 = clf2.fit(fsm,np.reshape(lsm,(-1,1)))
clf3 = tree.DecisionTreeClassifier()
clf3 = clf3.fit(ftm,np.reshape(ltm,(-1,1)))
clf4 = tree.DecisionTreeClassifier()
clf4 = clf4.fit(ffom,np.reshape(lfom,(-1,1)))
if len(lfom)==1:
	clf4 = clf4.fit(ffom,np.reshape(lfom,(-1,1)))

#now time to play the game
for i in range(0,1):
	n = 0
	boardList = [0,1,2,3,4,5,6,7,8]
	learnList = [[],[],[],[]]
	printBoard(boardList)
	newMoveList = []
	gameOn = True
	while gameOn == True:
		if n == 4:
			break #gonnna keep this random here for random testing
		#move = random.randint(0,9)
		#while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
		#	move = random.randint(0,9)
		move = int(input(" enter the number of the space you wish to fill "))
		while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
			move = int(input("spots taken though, so enter the number of the space you wish to fill "))
		boardList[move] = 'x'
		learnList[n].append(move)
		printBoard(boardList)
		gameOn = checkwin(boardList)
		if gameOn == False:
			break
		if n == 0:
			move = clf1.predict(np.reshape(learnList[0][0],(-1,1)))
		elif n==1:
			prep = learnList[1]
			#prep.pop()
			move = clf2.predict(np.reshape(learnList[0]+prep,(1,-1)))
		elif n == 2:
			prep = learnList[2]
			#prep.pop()
			move = clf3.predict(np.reshape(learnList[0]+learnList[1]+prep,(1,-1)))
		elif n==3:
			prep = learnList[3]
			#prep.pop()
			move = clf4.predict(np.reshape(learnList[0]+learnList[1]+learnList[2]+prep,(1,-1)))
		print(" the move the computer wants you to enter is ",end = "")
		print(move)
		move = int(input(" enter the computers command, if its not there just enter any number "))
		while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
			move = int(input("spots taken though, so enter the number of the space you wish to fill "))
		boardList[move] = 'o'
		learnList[n].append(move)
		printBoard(boardList)
		gameOn = checkwin(boardList)
		n+=1
