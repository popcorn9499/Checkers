class display():
	def clearScreen(self): #kinda obvious
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


	def infoPanel(self): 
		info = '''
O = Red Men			
I = Red King
L = Black Men
K = Black King
_ = Valid Spaces

		'''
		print(info)

	def start(self,board): #draws the board
		self.clearScreen()
		self.drawLetters()
		self.drawBoard(board)
		self.infoPanel()



	



