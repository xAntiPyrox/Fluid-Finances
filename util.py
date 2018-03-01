#######################################
# Utilities File                      #
#######################################

import os

class Program:
	def __init__(self, version):
		self.running = True
		self.version = version

	def clearScreen(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def isRunning(self):
		return self.running

	def stop(self):
		self.running = False

	def greeting(self):
		self.clearScreen()
		print("Welcome to Fluid Finances version" + self.version + "\n") 
		print("Balance = ???")

	def handleInput(self, userInput):
		if userInput == "quit":
			self.stop()
		elif userInput == "exit":
			self.stop()
		elif userInput == "clear":
			self.clearScreen()
		elif userInput == "help":
			print("List of available commands: \n" +
				  "quit/exit: Ends the program\n" +
				  "clear: Clears all text on the screen\n" +
				  "help: List all available commands")
		else:
			print(userInput + " is not a valid command")


