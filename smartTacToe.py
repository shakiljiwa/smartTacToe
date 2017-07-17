import random #to train the model, it will be able to play against randomly generated moves or the player herself
def printboard(boardlist): # this is just a method that takes the list which is the x and o grid and prints it
	for n in range(0,8,3):
		print("   ",end = "")
		print(boardlist[n], end = "  |  ")
		print(boardlist[n+1], end = "  |  ")
		print(boardlist[n+2])
		if n != 6:
			print("--------------------") #just for visuals

def pvp(): #this is a player vs player module that will be a base for the game and its testing
	boardlist = [0,1,2,3,4,5,6,7,8]
	printboard(boardlist)
	gameOn = True
	while gameOn == True:
		boardlist = move(boardlist,'x')
		printboard(boardlist)
		gameOn = checkwin(boardlist)
		if gameOn == False:
			break
		boardlist = move(boardlist,'o')
		printboard(boardlist)
		gameOn = checkwin(boardlist)
		
def move(boardlist,player):
	move = int(input(player + " enter the number of the space you wish to fill "))
	while move not in boardlist: #to ensure a spot doesnt get filled then filled again by another or the same player
		move = int(input("spots taken though, so enter the number of the space you wish to fill "))
	boardlist[move] = player
	return boardlist

def checkwin(boardlist):
	for n in range(0,7,3):
		if boardlist[n] == boardlist[n+1] and boardlist[n] == boardlist[n+2]:
			print("the winner is... " + boardlist[n] )
			#addpoint(n)
			return False
	for n in range(0,3):
		if boardlist[n]== boardlist[n+3] and boardlist[n]== boardlist[n+6]:
			print("the winner is... " + boardlist[n] )
			#addpoint(n)
			return False
	if (boardlist[2] == boardlist[4] and boardlist[2]== boardlist[6]) or (boardlist[0] == boardlist[4] and boardlist[0]== boardlist[8]):
		print("the winner is... " + boardlist[n] )
		#addpoint(n)
		return False
		
	else:
		return True
pvp()
		
		
		
		
