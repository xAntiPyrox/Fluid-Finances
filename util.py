#######################################
# Utilities File                      #
#######################################

# import necessary modules
import os
import datetime

### Program class with all commands ###
class Program:
	# constructor
	def __init__(self, version):
		self.running = True
		self.version = version

	# clear the screen (works on unix and windows)
	def clearScreen(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	# returns true of the program is running, false otherwise
	def isRunning(self):
		return self.running

	# stops program execution and clears screen
	def stop(self):
		self.running = False
		self.clearScreen()

	# initial message when starting the program
	def greeting(self):
		self.clearScreen()
		print("Welcome to Fluid Finances version " + self.version + "\n") 
		print("Balance = ???")

	# get input from the user and split it into a list
	def getInput(self):
		userInput = input("\n>>> ")
		return userInput.split()

	# take user input and determine which command to run
	def handleInput(self, userInput):
		if userInput[0] == "quit":
			self.stop()
		elif userInput[0] == "exit":
			self.stop()
		elif userInput[0] == "clear":
			self.clearScreen()
		elif userInput[0] == "transactions":
			self.viewTransactions(userInput)
		elif userInput[0] == "new":
			self.new(userInput)
		elif userInput[0] == "help":
			print("List of available commands: \n" +
				  "transactions:\t\tView transactions for a specified week\n" +
				  "quit/exit:\t\tEnds the program\n" +
				  "clear:\t\t\tClears all text on the screen\n" +
				  "help:\t\t\tList all available commands")
		else:
			print(userInput[0] + " is not a valid command")

	# view transactions, done for current week if a date isn't given
	def viewTransactions(self, userInput):
		if len(userInput) > 1: # pass date if it was given
			date = userInput[1].split('/')
			week = Week(date[0], date[1], date[2])
		else: # default to current week
			week = Week()

		# print the dates being covered
		print("Showing transactions for " + week.toString(0) + " to " + week.toString(6))

	# modular command for new things
	def new(self, userInput):
		if len(userInput) < 2:
			print("'new' requires additional parameters\n" +
				  "transaction:\t\tAdd a new transaction")
		else:
			if userInput[1] == "transaction":
				self.newTransaction(userInput)

	def newTransaction(self, userInput):
		if len(userInput) < 3:
			date = input("Date: ")
			payee = input("Payee: ")
			withdrawl = input("Withdrawl? (yes/no): ")
			amount = input("Amount: ")
		else:
			date = userInput[2]
			payee = userInput[3]
			withdrawl = userInput[4]
			amount = userInput[5]

		if withdrawl == "yes" or "y" or "YES" or "Yes":
			action = "was paid to"
		else:
			action = "was recieved from"

		print("On " + date + ", " + amount + " " + action + " " + payee) 

### Maintains information for working within a specific week ###
class Week:
	# constructor
	def __init__(self, month = None, day = None, year = None):
		if month is None and day is None and year is None:
			# use today's date if none was given
			self.date = datetime.date.today()
		else:
			# use a given date
			self.date = datetime.date(int(year), int(month), int(day))

		# determine monday and sunday of the week for the date used
		self.monday = self.date - datetime.timedelta(days = self.date.weekday())
		self.sunday = self.date + datetime.timedelta(days = 7 - self.date.weekday())

	# returns date of given day (defaults to current day) in MM/DD/YYYY format
	def toString(self, weekday = None):
		if weekday == None:
			# give today if none was given
			month = self.date.month
			day = self.date.day
			year = self.date.year
		else:
			# give the specified day (0 = monday)
			currentDate = self.monday + datetime.timedelta(days = weekday)
			month = currentDate.month
			day = currentDate.day
			year = currentDate.year

		return str(month) + "/" + str(day) + "/" + str(year)
