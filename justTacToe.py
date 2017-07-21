import random #to train the model, it will be able to play against randomly generated moves or the player herself
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
	toLearnFrom = []
	for n in range(0,1):	
		n = 0
		boardList = [0,1,2,3,4,5,6,7,8]
		learnList = [[],[],[],[]]
		printBoard(boardList)
		gameOn = True
		while gameOn:
			newMoveList = randomMove(boardList,'x')
			if n<4:
				learnList[n].append(extractMove(boardList,newMoveList)) #stupid oop because im lazy
			boardList = newMoveList
			printBoard(boardList)
			gameOn = checkwin(boardList,learnList)
			if n == 4:
				break
			if gameOn == False:
				break
			newMoveList = randomMove(boardList,'o')
			learnList[n].append(extractMove(boardList,newMoveList)) 
			boardList = newMoveList
			printBoard(boardList)
			gameOn = checkwin(boardList, learnList)
			n+=1
		toLearnFrom.append(whoWin)
def extractMove(boardList, newMoveList):
	for i in range(0,len(boardList)):
		if boardList[i]!= newMoveList[i]:
			return i

def move(boardList,player): #this move method is for manual play
	move = int(input(player + " enter the number of the space you wish to fill "))
	while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
		move = int(input("spots taken though, so enter the number of the space you wish to fill "))
	boardList[move] = player
	return boardList

def randomMove(boardList,player): #in this case the player makes a random move
	print("the other player makes a random move")
	move = random.randint(0,9)
	while move not in boardList: #to ensure a spot doesnt get filled then filled again by another or the same player
		move = random.randint(0,9)
	boardList[move] = player
	return boardList

def checkwin(boardList,learnList):
	for n in range(0,7,3):
		if boardList[n] == boardList[n+1] and boardList[n] == boardList[n+2]:
			print("the winner is... " + boardList[n] )
			return False
	for n in range(0,3):
		if boardList[n]== boardList[n+3] and boardList[n]== boardList[n+6]:
			print("the winner is... " + boardList[n] )
			return False
	if (boardList[2] == boardList[4] and boardList[2]== boardList[6]) or (boardList[0] == boardList[4] and boardList[0]== boardList[8]):
		print("the winner is... " + boardList[n] )
		return False
		
	else:
		return True
		
def whoWin(boardList,learnList):
	for n in range(0,7,3):
		if boardList[n] == boardList[n+1] and boardList[n] == boardList[n+2]:
			print("the winner is... " + boardList[n] )
			if boardList[n]=='o':
				return learnList
	for n in range(0,3):
		if boardList[n]== boardList[n+3] and boardList[n]== boardList[n+6]:
			print("the winner is... " + boardList[n] )
			if boardList[n]=='o':
				return learnList
	if (boardList[2] == boardList[4] and boardList[2]== boardList[6]) or (boardList[0] == boardList[4] and boardList[0]== boardList[8]):
		print("the winner is... " + boardList[n] )
		if boardList[n]=='o':
				return learnList
		
	else:
		return None
		
pvp()
		
		
		
		
