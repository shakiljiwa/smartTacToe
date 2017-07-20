import random #to train the model, it will be able to play against randomly generated moves or the player herself
from sklearn import tree
def printboard(boardlist): # this is just a method that takes the list which is the x and o grid and prints it
	for n in range(0,8,3):
		print("   ",end = "")
		print(boardlist[n], end = "  |  ")
		print(boardlist[n+1], end = "  |  ")
		print(boardlist[n+2])
		if n != 6:
			print("--------------------") #just for visuals

def pvp(): #this is a player vs player module that will be a base for the game and its testing
	tolearnfrom = []
	for n in range(0,1):	
		n = 0
		boardlist = [0,1,2,3,4,5,6,7,8]
		learnList = [[],[],[],[]]
		printboard(boardlist)
		gameOn = True
		while gameOn == True:
			newMoveList = randomMove(boardlist,'x')
			if n<4:
				learnList[n].append(extractMove(boardlist,newMoveList)) #stupid oop because im lazy
			boardlist = newMoveList
			printboard(boardlist)
			gameOn = checkwin(boardlist,learnList)
			if n == 4:
				break
			if gameOn == False:
				break
			newMoveList = randomMove(boardlist,'o')
			learnList[n].append(extractMove(boardlist,newMoveList)) 
			boardlist = newMoveList
			printboard(boardlist)
			gameOn = checkwin(boardlist, learnList)
			n+=1
		tolearnfrom.append(whoWin)
def extractMove(boardlist, newMoveList):
	for i in range(0,len(boardlist)):
		if boardlist[i]!= newMoveList[i]:
			return i

def move(boardlist,player): #this move method is for manual play
	move = int(input(player + " enter the number of the space you wish to fill "))
	while move not in boardlist: #to ensure a spot doesnt get filled then filled again by another or the same player
		move = int(input("spots taken though, so enter the number of the space you wish to fill "))
	boardlist[move] = player
	return boardlist

def randomMove(boardlist,player): #in this case the player makes a random move
	print("the other player makes a random move")
	move = random.randint(0,9)
	while move not in boardlist: #to ensure a spot doesnt get filled then filled again by another or the same player
		move = random.randint(0,9)
	boardlist[move] = player
	return boardlist

def checkwin(boardlist,learnList):
	for n in range(0,7,3):
		if boardlist[n] == boardlist[n+1] and boardlist[n] == boardlist[n+2]:
			print("the winner is... " + boardlist[n] )
			return False
	for n in range(0,3):
		if boardlist[n]== boardlist[n+3] and boardlist[n]== boardlist[n+6]:
			print("the winner is... " + boardlist[n] )
			return False
	if (boardlist[2] == boardlist[4] and boardlist[2]== boardlist[6]) or (boardlist[0] == boardlist[4] and boardlist[0]== boardlist[8]):
		print("the winner is... " + boardlist[n] )
		return False
		
	else:
		return True
		
def whoWin(boardlist,learnList):
	for n in range(0,7,3):
		if boardlist[n] == boardlist[n+1] and boardlist[n] == boardlist[n+2]:
			print("the winner is... " + boardlist[n] )
			if boardlist[n]=='o':
				return learnList
	for n in range(0,3):
		if boardlist[n]== boardlist[n+3] and boardlist[n]== boardlist[n+6]:
			print("the winner is... " + boardlist[n] )
			if boardlist[n]=='o':
				return learnList
	if (boardlist[2] == boardlist[4] and boardlist[2]== boardlist[6]) or (boardlist[0] == boardlist[4] and boardlist[0]== boardlist[8]):
		print("the winner is... " + boardlist[n] )
		if boardlist[n]=='o':
				return learnList
		
	else:
		return None
		
pvp()
		
		
		
		
