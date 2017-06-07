
import urllib2
import os
from random import randint

fileName = "sowpods.txt"
correctLetters = []

#==================================================================================================
# Write data to the file
#==================================================================================================
def writeToFile(data):

	global fileName
	f = open(fileName,"w")

	for line in data:

		f.write(line)
	f.close

#==================================================================================================
# Find how many words there are in the file
#==================================================================================================
def getWordCount():

	global fileName
	with open(fileName, "r") as f:
		
		for i, l in enumerate(f):
			pass
	return i

#==================================================================================================
# search for word in the list that matches the line number
#==================================================================================================
def findWord(searchKey):

	global fileName
	with open(fileName, "r") as f:

		for i, l in enumerate(f):

			if(i == searchKey):
				return l


#==================================================================================================
# Search if the letter that was entered by the user is in the word
#==================================================================================================
def searchLetter(word, letterChoice):

	global correctLetters
	beginSearch = 0

	# Search for letter. If word is not found then the function returns -1
	letterIndex = word.find(letterChoice,beginSearch)
	if letterIndex == -1:
		print "Incorrect!"

	while (letterIndex != -1):
		
		# If we haven't already added this letter to the list of correct letters then add it
		# Shift start point of search by 1 position
		if letterIndex not in correctLetters:
			
			correctLetters.append(letterIndex)
			beginSearch = letterIndex + 1
		else:
			letterIndex = -1

		letterIndex = word.find(letterChoice,beginSearch)
	if beginSearch == 0:
		return False


#==================================================================================================
# Print out the word
#==================================================================================================
def printLetters(word):

	global correctLetters
	unfinishedWord=""

	for index, letter in enumerate(word):
		
		# Use the index of the letter to check if the user guessed correctly
		if index in correctLetters:
			unfinishedWord = unfinishedWord + letter + " "
		else:
			unfinishedWord = unfinishedWord + "_ "

	return unfinishedWord

#==================================================================================================
# Check if the user guessed the entire word
#==================================================================================================
def isFinished(unfinishedWord):

	c="_"
	if c in unfinishedWord:
		return False
	else:
		return True

#==================================================================================================
# Prints out the hanging man depending on how many guesses are remaining
#==================================================================================================
def showHangman(guessLimit):
# def showHangman():
	
	# print " ____"
	# print " |  |"
	# print " O  |"
	# print "/|\ |"
	# print "/ \ |"
	# print "   _|_"

	errors = {
		6: " ____\n |  |\n    |\n    |\n    |\n   _|_",
		5: " ____\n |  |\n O  |\n    |\n    |\n    |\n   _|_",
		4: " ____\n |  |\n O  |\n/   |\n    |\n    |\n   _|_",
		3: " ____\n |  |\n O  |\n/|  |\n    |\n    |\n   _|_",
		2: " ____\n |  |\n O  |\n/|\ |\n    |\n    |\n   _|_",
		1: " ____\n |  |\n O  |\n/|\ |\n/   |\n    |\n   _|_",
		0: " ____\n |  |\n O  |\n/|\ |\n/ \ |\n    |\n   _|_"
	}

	print errors[guessLimit]



def main():

	# If the file doesn't exist then get data from address and save it in the file
	if os.path.isfile("sowpods.txt") == False:
		
		# Get data from website and write to a file
		print "The file does not exist"
		urlTarget = "http://norvig.com/ngrams/sowpods.txt"
		data = urllib2.urlopen(urlTarget).read()
		writeToFile(data)
		

	wordCount = getWordCount()
	print "The " + fileName + " file contains " + str(wordCount) + " words."

	# Randomly pick a line number for a word 
	searchKey = randint(1,wordCount)
	wordChoice = findWord(searchKey).strip()
	# print "The word chosen is " + str(wordChoice).strip() + ". This is word number " + str(searchKey) + " in the list."

	wordLength = len(wordChoice)
	unfinishedWord =""
	done = False
	guessedLetters = set()
	guessLimit = 6
	isFound = False

	print "Welcome to Hangman!"
	print "_ " * wordLength
	print wordChoice

	while (done == False) and (guessLimit > 0):

		showHangman(guessLimit)
		letterChoice = str.upper(raw_input())
		if letterChoice in guessedLetters:
			print "You already guessed the letter " + letterChoice
		else:

			guessedLetters.add(letterChoice)

			isFound = searchLetter(wordChoice, letterChoice)
			if isFound == False:
				guessLimit -= 1
			print "You can make " + str(guessLimit) + " guesses. Good Luck :-)"

			# print correctLetters
			unfinishedWord = printLetters(wordChoice)

			done = isFinished(unfinishedWord)
			

		print unfinishedWord

	if done == True:
		print "Congrats!! You solved the word!!"
	else:
		showHangman(guessLimit)
		print "Aww looks like you weren't able to get it :-("
		print "The word is " + wordChoice


if __name__ == "__main__":
	main()
	# showHangman()