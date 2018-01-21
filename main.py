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
#this declares the debug mode information
global debugMode
debugMode = False
import display



def debugInfo(Message): #creates for the purpose of debugging when it is needed. makes my life easier instead of adding all my print statements back in
	if debugMode:
		print(Message)

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

def movePiece(board,x1,y1,x2,y2): #moves the piece
	guyDetails = board[int(y1)][int(x1)] 
	board[int(y1)][int(x1)]  = {"Color": "Valid", "Type": "Valid"}
	board[int(y2)][int(x2)] = guyDetails
	return board


def canDouble(x2,y2): #checks if a double jump can be performed
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

def isValidJump(board,x1,y1,x2,y2): #checks if the jump is valid
	debugInfo("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x1,y1,x2,y2))
	if x2 > 7 or x2 < 0 or y2 > 7 or y2 < 0:
		return False
	debugInfo("Check validity")
	debugInfo("X3: {0} y3: {1}".format(int(abs((y1+y2)/2)),int(abs(x1+x2)/2)))
	if board[y1][x1]["Type"] == "Men" and board[int(abs((y1+y2)/2))][int(abs((x1+x2)/2))]["Type"] == "Men":
		
		if abs(x1-x2) != 2 or abs(y1-y2) != 2: #checks if the move wanted is the right amount of spaces away or not
			debugInfo("Not enough spaces")
			return False

		debugInfo("Check valid spaces")

		if board[y2][x2]["Type"] != "Valid": #basically checks if the spot the user wants to move isnt ocupied and therefor valid
			debugInfo("Not valid space")
			return False
		if board[y2][x2]["Type"] == "Invalid":
			return False

		debugInfo("got to king checks and such")
		#these checks r to check if the user isnt a king and checks against the valid moves it can do
		if (y2 > y1) == False and playerTurn == "Red" and board[y1][x1]["Type"] != "King":
			return False
		elif (y2 < y1) == False and playerTurn == "Black" and board[y1][x1]["Type"] != "King":
			return False
		if board[int(abs((y1+y2)/2)) ][int(abs((x1+x2)/2) )]["Color"] == pieceColor(board,x1,y1): #color?
			return False

		if board[int(abs((y1+y2)/2)) ][int(abs((x1+x2)/2) )]["Type"] == "Valid": #color? 
			return False
		debugInfo("USER X Y {0}".format(board[y1][x1]["Color"]))
		debugInfo("USER X3 Y3 {0}".format(board[int(abs((y1+y2)/2)) ][int(abs((x1+x2)/2))]["Color"]))
		debugInfo("User must jump x: {0} y: {1} x2: {2} y2: {3}".format(x1,y1, x2, y2))
		return True

def pieceColor(board,x,y):#gets the piece color
	return board[y][x]["Color"]





def isValidMove(board,playerTurn,x1,y1,x2,y2): #checks if the move is valid
	debugInfo("X1: {0} Y1: {1}".format(x1,y1))
	if board[y2][x2]["Type"] == "Invalid":
		return False
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
				if debugMode == True:
					debugInfo("User must jump x: {0} y: {1}".format(x,y))
				return True



def tryJump(board,playerTurn,x1,y1,x2,y2): #attempts to do the jump the user wants to do
	if abs(x1-x2) != 2 or abs(y1-y2) != 2: #checks first if its the right number of spaces away.
		debugInfo("Invalid jump ammount")
		returnValues = [False,board]
		return returnValues

	if isValidJump(board,x1,y1,x2,y2): #checks if its a valid jump using this function
		debugInfo("Valid")
		board = movePiece(board,x1,y1,x2,y2)
		board[int(abs((y1+y2)/2))][int(abs((x1+x2)/2))] = {"Color": "Valid", "Type": "Valid"}
		while canDouble(x2,y2):
			display.display().start(board)
			debugInfo("Double")
			changeState ,board, x3, y3 = getInput(board,playerTurn,x2,y2)
			if changeState:
				x2 = x3
				y2 = y3
		board = kingMe(board,playerTurn,x2,y2)
		returnValues = [True,board]
		return returnValues
	debugInfo("Nothing applied")
	returnValues = [False,board]
	return returnValues




def tryMove(board,playerTurn,x1,y1,x2,y2): #attempts to see if a move is possibile.
	if abs(x1-x2) != 1 and abs(y1-y2):
		returnValues = [False,board]
		return returnValues
	if anyJumps(board,playerTurn):
		debugInfo("Must Jump!!!")
		returnValues = [False,board]
		return returnValues
	if isValidMove(board,playerTurn,x1,y1,x2,y2):
		board = movePiece(board,x1,y1,x2,y2)
		board = kingMe(board,playerTurn,x2,y2)
		returnValues = [True,board]
		return returnValues
	returnValues = [False,board]
	return returnValues


def isKing(board,x,y): #checks if the piece is a king or not
	if board[y][x]["Type"] == "King":
		return True
	else:
		return False

def kingMe(board,playerTurn,x,y):#Finds users that should be kinged
	debugInfo("Kinged Check")
	if playerTurn == "Red" and board[y][x]["Type"] == "Men" and y == 7:
		board[y][x]["Type"] = "King"
		debugInfo("Kinged")
	elif playerTurn == "Black" and board[y][x]["Type"] == "Men" and y == 0:
		board[y][x]["Type"] = "King"
		debugInfo("Kinged")
	return board



def switchTurn(playerTurn):
	if playerTurn == "Black":
		playerTurn = "Red"
	else:
		playerTurn = "Black"
	return playerTurn

def waitPlayer(board,playerTurn): #this is for waiting for the player and doing all the checks required from it
	board,playerTurn = getInput(board,playerTurn,-1,-1)
	return board,playerTurn


def getInput(board,playerTurn,xPos1,yPos1):
	print("Input")
	userInput = input().lower()
	userInput = userInput.split()
	if userInput[0] == "move" and xPos1 == -1 and yPos1 == -1:
		try:
			xPos1 = int(ord(userInput[1][1:]) - 97)
			yPos1 = int(userInput[1][:1])
			xPos2 = int(ord(userInput[2][1:]) - 97)
			yPos2 = int(userInput[2][:1])
			if board[yPos1][xPos1]["Color"] != "Valid" and board[yPos1][xPos1]["Color"] == playerTurn:
				returnValues = tryMove(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
				if returnValues[0] == False:
					debugInfo("Move Failed")
					returnValues = tryJump(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
					if returnValues[0]:
						board = returnValues[1]
						playerTurn = switchTurn(playerTurn)
						if debugMode == False: #this just draws the board unless debug mode is on
							display.display().start(board)
				else:
					debugInfo("Move Sucessful")
					board = returnValues[1]
					playerTurn = switchTurn(playerTurn)
					if debugMode == False: #this just draws the board unless debug mode is on
						display.display().start(board)
		except IndexError:
			print("Please read the instructions")

	
	elif userInput[0] =="move" and xPos1 != -1 and yPos1 != -1: #this move is only done when the game is in jump mode where the user must jump every space required
		try:
			xPos2 = int(ord(userInput[1][1:]) - 97)
			yPos2 = int(userInput[1][:1])
			returnValues = tryJump(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
			if returnValues[0]:
				board = returnValues[1]
				playerTurn = switchTurn(playerTurn)
				return True,board,xPos2,yPos2
			return False,board,xPos2,yPos2
		except IndexError:
					print("Please read the instructions")
					return False,board,xPos2,yPos2


	elif userInput[0] == "find" and debugMode: #testing
		xPos = ord(userInput[1][1:]) - 97
		yPos = userInput[1][:1]-1
		print(board[int(yPos)][int(xPos)])
	elif userInput[0] == "changeturn" and debugMode:
		playerTurn = switchTurn(playerTurn)
	elif userInput[0] == "draw":
		display.display().start(board)
	return board,playerTurn







board = createBoard()

display.display().start(board) #draws the board
while True:
	board,playerTurn = waitPlayer(board,playerTurn) #starts the actual game
