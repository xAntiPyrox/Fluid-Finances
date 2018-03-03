#######################################
# Fluid Finances                      #
# Main file for running program       #
# Created 2/28/2018                   #
#######################################

import util

# main function
program = util.Program("Alpha 0.1")

program.greeting()
while (program.isRunning() is True):
	userInput = program.getInput()
	program.handleInput(userInput)
