#coding: utf-8
import random

def play():
	dieA = random.randint(1,6)
	dieB = random.randint(1,6)
	diceSum = dieA + dieB
	i = 1
	winPoint = 0
	winLose = 0
	#print 'Dice sum is : ', diceSum
	if i == 1 and (diceSum == 7 or diceSum == 11) :
		#print 'Player Wins on first roll.'
		return 1
	elif i == 1 and (diceSum == 2) or (diceSum == 3) or (diceSum == 12):
		#print 'Player Loses on first roll.'
		return -1
	elif i == 1 :
		i = i + 1
		winPoint = diceSum
		#print 'Winning Point is ', winPoint
		while winLose == 0 :
			#print 'Player rolls dice again...'
			dieA = random.randint(1,6)
			dieB = random.randint(1,7)
			diceSum = dieA + dieB
			#print 'Dice sum is : ', diceSum
			if diceSum == winPoint :
				#print 'Player Wins on roll number ', i
				winLose = 1
				return i
			elif diceSum == 7 :
				#print 'Player Loses on roll number ', i
				winLose = 1
				return -i
			i = i + 1

