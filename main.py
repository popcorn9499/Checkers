# display should parse the string each row at a time
# each row in between a tile should be filled with dashes

'''
[x][y] = {"Color": "", "Type": ""}
Color can = "Red" or "Black"
Type can = "Knight" or "Men", "Invalid"

O = Red Men
I = Red Knight
L = Black Men
K = Black Knight


'''
playerTurn = "Black"

import display
def createBoard(): #creates the initial board array
	board = []
	for y in range(0,9):
		board.append(createBoardX(y))
	return board

def createBoardX(y): #this creates the horizontal colum 
	boardDetails = []
	for x in range(0,8):
		boardDetails.append({"Color": "Valid", "Type": "Valid"})
		if y % 2 == 1: #odd
			if x % 2 == 1: #odd
				if y < 3:
					boardDetails[x] = {"Color": "Red", "Type": "Men"}
				elif y > 4:
					boardDetails[x] = {"Color": "Black", "Type": "Men"}
			else:
				boardDetails[x] = {"Color": "Valid", "Type": "Invalid"}
		elif y % 2 == 0: #even
			if x % 2 == 0: #even
				if y < 3:
					boardDetails[x] = {"Color": "Red", "Type": "Men"}
				elif y > 4:
					boardDetails[x] = {"Color": "Black", "Type": "Men"}
			else:
				boardDetails[x] = {"Color": "Valid", "Type": "Invalid"}
	return boardDetails

def movePiece(board,x1,y1,x2,y2): #
	guyDetails = board[int(y1)][int(x1)] 
	board[int(y1)][int(x1)]  = {"Color": "Valid", "Type": "Valid"}
	board[int(y2)][int(x2)] = guyDetails
	return board


def canDouble(x2,y2):
	if isValidJump(board,x2,y2,x2+2,y2+2):
		print("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2+2,y2+2))
		return True
	elif isValidJump(board,x2,y2,x2-2,y2+2):
		print("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2-2,y2+2))
		return True
	elif isValidJump(board,x2,y2,x2+2,y2-2):
		print("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2+2,y2-2))
		return True
	elif isValidJump(board,x2,y2,x2-2,y2-2):
		print("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2-2,y2-2))
		return True

def isValidJump(board,x1,y1,x2,y2):
	print("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x1,y1,x2,y2))
	if x2 > 7 or x2 < 0 or y2 > 7 or y2 < 0:
		return False
	if board[y1][x1]["Type"] == "Men" and board[int(abs((y1+y2)/2))][int(abs((x1+x2)/2))]["Type"] == "Men":
		
		if abs(x1-x2) != 2 or abs(y1-y2) != 2: #checks if the move wanted is the right amount of spaces away or not
			print("Not enough spaces")
			return False



		if board[y2][x2]["Type"] != "Valid": #basically checks if the spot the user wants to move isnt ocupied and therefor valid
			print("Not valid space")
			return False
		if board[y2][x2]["Type"] == "Invalid":
			return False

		abs(x1+x2/2) 


		#these checks r to check if the user isnt a king and checks against the valid moves it can do
		if (y2 > y1) == False and playerTurn == "Red" and board[y1][x1]["Type"] != "King":
			return False
		elif (y2 < y1) == False and playerTurn == "Black" and board[y1][x1]["Type"] != "King":
			return False
		if board[int(abs((y1+y2)/2)) ][int(abs((x1+x2)/2) )]["Color"] == pieceColor(board,x1,y1): #color?
			return False

		if board[int(abs((y1+y2)/2)) ][int(abs((x1+x2)/2) )]["Type"] == "Valid": #color?
			return False
		print("USER X Y {0}".format(board[y1][x1]["Color"]))
		print("USER X3 Y3 {0}".format(board[int(abs((y1+y2)/2)) ][int(abs((x1+x2)/2))]["Color"]))
		print("User must jump x: {0} y: {1} x2: {2} y2: {3}".format(x1,y1, x2, y2))
		return True

def pieceColor(board,x,y):
	return board[y][x]["Color"]





def isValidMove(board,playerTurn,x1,y1,x2,y2): #checks if the move is valid
	print("X1: {0} Y1: {1}".format(x1,y1))
	if board[y2][x2]["Color"] != "Valid": #check if the second spot is a filled space with anything
		return False
	if playerTurn == "Red" and board[y1][x1]["Type"] != "King":
		return y2 > y1
	elif playerTurn == "Black" and board[y1][x1]["Type"] != "King":
		return y2 < y1
	if board[y1][x1]["Type"] == "King":
		return True
	return False


def anyJumps(board,playerTurn): #check to see if any jump exists
	for x in range(0,7):
		for y in range(0,7):
			if canDouble(x,y) and board[y][x]["Color"] == playerTurn:
				print("User must jump x: {0} y: {1}".format(x,y))
				return True



def tryJump(board,playerTurn,x1,y1,x2,y2):
	if abs(x1-x2) != 2 or abs(y1-y2) != 2:
		returnValues = [True,board]
		return returnValues

	if isValidJump(board,x1,y1,x2,y2):
		print("Valid")
		board = movePiece(board,x1,y1,x2,y2)
		board[int(abs((y1+y2)/2))][int(abs((x1+x2)/2))] = {"Color": "Valid", "Type": "Valid"}
		
		while canDouble(x2,y2):
			x = x1
			y = y1
			
			display.display().start(board)
			print("Double")
			changeState ,board, x3, y3 = getInput(board,playerTurn,x2,y2)
			if changeState:
				x2 = x3
				y2 = y3
			
		returnValues = [True,board]
		return returnValues



def tryMove(board,playerTurn,x1,y1,x2,y2): #attempts to see if a move is possibile.
	if abs(x1-x2) != 1 and abs(y1-y2):
		returnValues = [False,board]
		return returnValues
	if anyJumps(board,playerTurn):
		print("Must Jump!!!")
		returnValues = [False,board]
		return returnValues
	if isValidMove(board,playerTurn,x1,y1,x2,y2):
		board = movePiece(board,x1,y1,x2,y2)
		returnValues = [True,board]
		return returnValues
	returnValues = [False,board]
	return returnValues


def isKing(board,x,y):
	if board[y][x]["Type"] == "King":
		return True
	else:
		return False


def switchTurn(playerTurn):
	if playerTurn == "Black":
		playerTurn = "Red"
	else:
		playerTurn = "Black"
	return playerTurn

def waitPlayer(board,playerTurn):
	board,playerTurn = getInput(board,playerTurn,-1,-1)
	return board,playerTurn


def getInput(board,playerTurn,xPos1,yPos1):
	print("Input")
	userInput = input()
	userInput = userInput.split()
	if userInput[0] == "Move" and xPos1 == -1 and yPos1 == -1:
		xPos1 = int(ord(userInput[1][1:]) - 97)
		yPos1 = int(userInput[1][:1])
		xPos2 = int(ord(userInput[2][1:]) - 97)
		yPos2 = int(userInput[2][:1])
		if board[yPos1][xPos1]["Color"] != "Valid" and board[yPos1][xPos1]["Color"] == playerTurn:
			returnValues = tryMove(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
			if returnValues[0] == False:
				print("Move Failed")
				returnValues = tryJump(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
				if returnValues[0]:
					board = returnValues[1]
					playerTurn = switchTurn(playerTurn)
			else:
				print("Move Sucessful")
				board = returnValues[1]
				playerTurn = switchTurn(playerTurn)
	
	elif userInput[0] =="Move" and xPos1 != -1 and yPos1 != -1:
		xPos2 = int(ord(userInput[1][1:]) - 97)
		yPos2 = int(userInput[1][:1])
		returnValues = tryJump(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
		if returnValues[0]:
			board = returnValues[1]
			playerTurn = switchTurn(playerTurn)
			return True,board,xPos2,yPos2
		return False,board,xPos2,yPos2


	elif userInput[0] == "Find": #testing
		xPos = ord(userInput[1][1:]) - 97
		yPos = userInput[1][:1]-1
		print(board[int(yPos)][int(xPos)])
	elif userInput[0] == "ChangeTurn":
		playerTurn = switchTurn(playerTurn)
	elif userInput[0] == "Draw":
		display.display().start(board)
	return board,playerTurn


board = createBoard()

#while True:
display.display().start(board)
while True:
	board,playerTurn = waitPlayer(board,playerTurn)


















	