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
debugMode = True
import display
import fileIO
import sys


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
					boardDetails[x] = {"Color": "Black", "Type": "King"}
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
		debugInfo("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2+2,y2+2))
		return True
	elif isValidJump(board,x2,y2,x2-2,y2+2):
		debugInfo("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2-2,y2+2))
		return True
	elif isValidJump(board,x2,y2,x2+2,y2-2):
		debugInfo("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2+2,y2-2))
		return True
	elif isValidJump(board,x2,y2,x2-2,y2-2):
		debugInfo("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x2,y2,x2-2,y2-2))
		return True

def isValidJump(board,x1,y1,x2,y2): #checks if the jump is valid
	debugInfo("X1: {0} Y1: {1} X2: {2} Y2: {3}".format(x1,y1,x2,y2))
	if x2 > 7 or x2 < 0 or y2 > 7 or y2 < 0:
		return False
	debugInfo("Check validity")
	debugInfo("X3: {0} y3: {1}".format(int(abs((y1+y2)/2)),int(abs(x1+x2)/2)))
	if pieceType(board,x1,y1) == "Men" or pieceType(board,x1,y1) == "King":#checks if the user is a king or a man in which case this is fine and continues

		if pieceType(board,int(abs((x1+x2)/2)),int(abs((y1+y2)/2))) == "Invalid" or pieceType(board,int(abs((x1+x2)/2)),int(abs((y1+y2)/2))) == "Valid": #checks if the space between point a and point b in which the user wants to jump has someone to jump
			return False



		if abs(x1-x2) != 2 or abs(y1-y2) != 2: #checks if the move wanted is the right amount of spaces away or not
			debugInfo("Not enough spaces")
			return False

		debugInfo("Check valid spaces")

		if pieceType(board,x2,y2) != "Valid": #basically checks if the spot the user wants to move isnt ocupied and therefor valid
			debugInfo("Not valid space")
			return False
		if pieceType(board,x2,y2) == "Invalid":
			return False

		debugInfo("got to king checks and such")
		#these checks r to check if the user isnt a king and checks against the valid moves it can do
		if (y2 > y1) == False and playerTurn == "Red" and pieceType(board,x1,y1) != "King":
			return False
		elif (y2 < y1) == False and playerTurn == "Black" and pieceType(board,x1,y1) != "King":
			return False
		if pieceColor(board,int(abs((x1+x2)/2) ),int(abs((y1+y2)/2))) == pieceColor(board,x1,y1): #color?
			return False

		if pieceType(board,int(abs((x1+x2)/2)),int(abs((y1+y2)/2))) == "Valid": #color? 
			return False
		debugInfo("USER X Y {0}".format(pieceColor(board,x1,y1)))
		debugInfo("USER X3 Y3 {0}".format(pieceColor(board,int(abs((x1+x2)/2) ),int(abs((y1+y2)/2)))))
		debugInfo("User must jump x: {0} y: {1} x2: {2} y2: {3}".format(x1,y1, x2, y2))
		return True

def pieceColor(board,x,y):#gets the piece color and returns it
	return board[y][x]["Color"]

def pieceType(board,x,y): #gets the piece type and returns it
	return board[y][x]["Type"]



def isValidMove(board,playerTurn,x1,y1,x2,y2): #checks if the move is valid
	debugInfo("X1: {0} Y1: {1}".format(x1,y1))
	if pieceType(board,x2,y2) == "Invalid":
		return False
	if pieceType(board,x2,y2) != "Valid": #check if the second spot is a filled space with anything
		return False
	if playerTurn == "Red" and pieceType(board,x1,y1) != "King":
		return y2 > y1
	elif playerTurn == "Black" and pieceType(board,x1,y1) != "King":
		return y2 < y1
	if pieceType(board,x1,y1) == "King":
		return True
	return False


def anyJumps(board,playerTurn): #check to see if any jump exists
	for x in range(0,7):
		for y in range(0,7):
			if canDouble(x,y) and pieceColor(board,x,y) == playerTurn:
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
			redLeft, blackLeft = getPiecesLeft(board)
			display.display().start(board,playerTurn,redLeft,blackLeft)
			debugInfo("Double")
			changeState ,board, x3, y3 = getInput(board,playerTurn,x2,y2) #repolls for input to get the user to get where the user wants to move to
			if changeState: #change state is just a variable 
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
		print("Must Jump!!")
		returnValues = [False,board]
		return returnValues
	if isValidMove(board,playerTurn,x1,y1,x2,y2):
		board = movePiece(board,x1,y1,x2,y2)
		board = kingMe(board,playerTurn,x2,y2)
		returnValues = [True,board]
		return returnValues
	returnValues = [False,board]
	return returnValues

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

def getPiecesLeft(board):
	redLeft = 0
	blackLeft = 0
	for x in range(0,8):
		for y in range(0,8):
			if pieceType(board,x,y) == "Men" or pieceType(board,x,y) == "King":
				if pieceColor(board,x,y) == "Red":
					redLeft += 1
				elif pieceColor(board,x,y) == "Black":
					blackLeft += 1
	return redLeft,blackLeft

def gameover(redLeft,blackLeft):#checks if game over or not
	if redLeft < 1:
		Print("Black Won")
		return True
	elif blackLeft < 1:
		print("Red Won")
		return True
	return False

def getInput(board,playerTurn,xPos1,yPos1):
	#get pieces left
	redLeft,blackLeft = getPiecesLeft(board)
	if gameover(redLeft,blackLeft): #checks if the game is over or not
		exit()	
	print("Input")
	userInput = input().lower()
	userInput = userInput.split()
	if userInput[0] == "move" and xPos1 == -1 and yPos1 == -1:
		try:
			xPos1 = int(ord(userInput[1][1:]) - 97)
			yPos1 = int(userInput[1][:1])
			xPos2 = int(ord(userInput[2][1:]) - 97)
			yPos2 = int(userInput[2][:1])
			if pieceColor(board,xPos1,yPos1) != "Valid" and pieceColor(board,xPos1,yPos1) == playerTurn:
				returnValues = tryMove(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
				if returnValues[0] == False:
					debugInfo("Move Failed")
					returnValues = tryJump(board,playerTurn,xPos1,yPos1,xPos2,yPos2)
					if returnValues[0]:
						board = returnValues[1]
						playerTurn = switchTurn(playerTurn)
						if debugMode == False: #this just draws the board unless debug mode is on
							display.display().start(board,playerTurn)
				else:
					debugInfo("Move Sucessful")
					board = returnValues[1]
					playerTurn = switchTurn(playerTurn)
					if debugMode == False: #this just draws the board unless debug mode is on
						display.display().start(board,playerTurn,redLeft,blackLeft)
		except (IndexError, TypeError,ValueError) as error:
			debugInfo('Error on line {}'.format(sys.exc_info()[-1].tb_lineno, type(error).__name__, error))
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
		except (IndexError, TypeError,ValueError) as e:
					print("Please read the instructions")
					return False,board,xPos2,yPos2

	elif userInput[0] == "save": #saves all the information on the board
		if userInput[1] != "":
			fileIO.saveBoard(userInput[1],board,playerTurn)
	elif userInput[0] == "load": #Loads alll the board information from a file
		if userInput[1] != "": 

			returnValues = fileIO.loadBoard(userInput[1])
			print(type(returnValues[0]))
			if type(returnValues[0]) == list: #Checks if the values returned was a list
				board = returnValues[0]
				playerTurn = returnValues[1]
				display.display().start(board,playerTurn,redLeft,blackLeft) #displays the new board information
				print("Loading")
			else:
				print("File doesnt exist")
		
	elif userInput[0] == "list":
		fileIO.listSaves()
	elif userInput[0] == "find" and debugMode: #testing
		xPos = ord(userInput[1][1:]) - 97
		yPos = userInput[1][:1]-1
		print(board[int(yPos)][int(xPos)])
	elif userInput[0] == "changeturn" and debugMode:
		playerTurn = switchTurn(playerTurn)
	elif userInput[0] == "draw":
		display.display().start(board,playerTurn,redLeft,blackLeft)
	elif userInput[0] == "quit":
		print("Closing...")
		exit()
	return board,playerTurn







board = createBoard()
redLeft,blackLeft = getPiecesLeft(board)
display.display().start(board,playerTurn,redLeft,blackLeft) #draws the board
while True:
	board,playerTurn = waitPlayer(board,playerTurn) #starts the actual game
