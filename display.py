import os
import sys
class display():
		
	def clearScreen(self): #kinda obvious
		if sys.platform == "linux" or sys.platform == "linux2":
			os.system('clear')
		if sys.platform == "win32":
			os.system('cls')
		else:
			for i in range(0,99):
			 	print("")

	def getChar(self,details): #Gets the character to display for the slot
		if details["Color"] == "Red":
			if details["Type"] == "Men":
				return "O"
			elif details["Type"] == "King":
				return "I"
		elif details["Color"] == "Black":
			if details["Type"] == "Men":
				return "L"
			elif details["Type"] == "King":
				return "K"
		return " "

	def drawBoard(self,board): #draws the board
		string = "" #creates the string that used for the entire board
		print("-"*35) 
		for y in range(0,8): #cycles through the array
			string += str(y) +" |"
			for x in range(0,8):
				if board[y][x]["Type"] != "Valid": #determines if its a valid square and if it isnt just valid and has something else do that
					string += self.getChar(board[y][x]) +  "  |"
				else:
					string += "_  |"
			
			print(string)
			print("-"*35)
			string = ""

	def drawLetters(self): #draws letters for the coordinates to move stuff to and pull from
		string = ""
		for i in range(0,8):
			if i == 0:
				string += "   "
			string += chr(97 + i) + "  |"
		print(string)


	def infoPanel(self,playerTurn,redLeft,blackLeft): 
		info = '''
Legend	            Information
O = Red Men	            Player {0}'s Turn
I = Red King            Red: {1}
L = Black Men           Black: {2}
K = Black King      Commands: Quit, Move, Save, Load, List
_ = Valid Spaces    to move a player type Move (starting space) (ending space) ex Move 1a 2b
                    ex Save (some file)
                    ex Save (some file that exists)


		'''.format(playerTurn,redLeft,blackLeft)
		print(info)

	def start(self,board,playerTurn,redLeft,blackLeft): #draws the board
		self.clearScreen()
		self.drawLetters()
		self.drawBoard(board)
		self.infoPanel(playerTurn,redLeft,blackLeft)



	



