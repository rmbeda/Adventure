# Author Robert Beda
# Last edited Wednesday, May 6, 2021
# Use Python 3.7

# How to use - Player:
# If the game designer has done their job properly,
# you should be able to play the game by just running
# this script using  Python 3.7. If you are unsure 
# how to do this, refer to the
# following steps (best suited for OS X users).

# - Make sure that Python 3.7 is installed on your computer.
# - Open a terminal program (such as Terminal on OS X)
# - In the terminal window, navigate to the directory 
# containing this script (the one you are reading). 
# You can do so in OS X Catalina by typing 'cd '
# (the space is important), dragging the folder
# containing this file from Finder into the Terminal
# window, and hitting 'enter'.
# - Run this script using Python 3.7. In OS X
# Catalina, this can be done by typing 'python3 Adventure.py'
# and hitting 'enter'.
# - Follow the instructions provided to proceed with
# the game.

# How to use - Game Designer:
# This Python script navigates through a 'Choose Your 
# Own Adventure' story in a computer terminal by 
# using the structure of computer directories.
# It should be stored in a directory along
# with two '.txt' files and a folder leading
# to a subdirectory that contains exactly one '.txt'
# file. One of the two files next to this script should 
# contain instructions for the player, while the other
# should contain information to be provided when they 
# exit the game.

# In this program, text scenes are read to the terminal 
# from '.txt' files. Hitting 'enter' to partition two lines
# when writing the '.txt' files will cause those lines
# to be separated by a line of whitespace when they are
# displayed in an OS X Catalina Terminal window.

# To organize the '.txt' files containing your scenes,
# follow the following example.

# If scene B follows as a possibility from scene A, 
# the '.txt' file containing scene B should be placed
# in a folder that is in the same directory as that of
# '.txt' file containing scene A. The player should be
# instructed in 'A.txt' to enter the name of the folder
# containing 'B.txt' in order to access that scene. Any
# folder names provided to the player as options should
# contain exactly one '.txt' file. Note that folder names
# are case-sensitive.

# To prepare this script, set the constants starting 
# on line 102. Make sure
# that the first three in particular match the other
# contents of this script's directory. Make sure that
# 'begin_options' and 'exit_options' are both non-empty
# lists, and that they match the instructions provided 
# in the '.txt' file with the name assigned to the 
# variable 'first_txt'. Finally, make sure that the
# messages that greet/bid farewell to the player are
# as you desire. They are the best places to provide
# them with the title of your story.

import os

def sep():
	print(' ')
	return None

def partition():
	print('#'*20)
	return None

def read(filename):
	sep()
	partition()
	f = open(filename, 'r')
	line = f.readline()
	print(line)
	x=1
	while x:
		line = f.readline()
		if line=='':
			x=0
		else:
			print(line)
	f.close()
	sep()
	return None

def sep_print(statement):
	sep()
	partition()
	print(statement)
	return None


#########
# Set Constants:

first_txt = 'Introduction.txt' # Name of '.txt' file with player instructions
last_txt = 'Credits.txt'       # Name of closing '.txt' file
first_folder = 'Scene1'        # Name of folder containing first scene

begin_options = ['Begin']      # Words players can use to begin the game
exit_options = ['exit', 'Exit'] # Words players can use to quit the game

game_title = 'The Serpent\'s Lair' # Title of your story
first_message = 'Hello! Welcome to {}'.format(game_title) 
# ^ Welcome message for players
completion_message = 'Thank you for completing {}'.format(game_title) 
# ^ Message when players complete the game
quit_message = 'Thanks for playing.'
 # ^ Message when players quit in the middle of a game

# That's all the constants to set.
######

# Main Script:
start = 0
complete = 0
home_dir = os.getcwd()


read(first_txt)
entry = input()
if entry in begin_options:
	os.chdir(first_folder)
	start = 1

while start:
	contents = os.listdir(os.getcwd())
	for thing in contents:
		if thing[-4:]=='.txt':
			read(thing)
			if thing[:3]=='End':
				moved = 1
				start = 0
				complete = 1
			else:
				moved = 0
	while not moved:
		move = input()
		if move in contents:
			os.chdir(move)
			moved = 1
		elif move in exit_options:
			moved = 1
			start = 0
		else:
			sep()
			print('That strand of fate is not accessible at this juncture. ' +\
                              'Select a different path.')     
			sep()
if complete:
	x = input('Enter your parting words: ')
	sep_print(completion_message)
else:
	sep_print(quit_message)
os.chdir(home_dir)
read(last_txt)



