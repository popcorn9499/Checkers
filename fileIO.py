import json
import os

#file load and save stuff
def fileSave(fileName,config):
	print("Saving")
	f = open(fileName, 'w') #opens the file your saving to with write permissions
	f.write(json.dumps(config,sort_keys=True, indent=4 ) + "\n") #writes the string to a file
	f.close() #closes the file io

def fileLoad(fileName):#loads files
	with open(fileName, 'r') as handle:#loads the json file
		config = json.load(handle) 
	return config

def saveBoard(fileName,board,playerTurn):
	if not os.path.exists("Saves"):#creates the saves folder
		os.makedirs("Saves")
	save = {"Board":board,"playerTurn":playerTurn} #
	fileSave("Saves/"+fileName+".save",save) #saves the information
	print("Saved")

def loadBoard(fileName):
	load = fileLoad("Saves/"+fileName+".save")
	board = load["Board"]
	playerTurn = load["playerTurn"]
	print("Loaded")
	return board,playerTurn

def listSaves():
	pass	