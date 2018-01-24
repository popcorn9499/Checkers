userInput = input().lower()
userInput = userInput.split()




def inputCheck(userInput):
	try: #checks if the user put in a1 for example
		x = int(userInput[1][:1])
		y = int(ord(userInput[1][1:]) - 97)
		return True,x,y
	except (TypeError,ValueError):
		try: #checks if the user put in 1a for example. returns none if the user didnt even follow that instruction
			x = int(ord(userInput[1][1:]) - 97)
			y = int(userInput[1][:1])
			return True,x,y
		except (TypeError,ValueError):
			return False,0,0

if userInput[0] == "move":
	if inputCheck(userInput[1]) != None: #if none dont go forward
		print(inputCheck(userInput[1]))
	

