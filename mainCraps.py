#coding utf-8
import craps

results = [0]*1000
gamesWon = [0]*21
gamesLost = [0]*21
probWin = 0
avgRolls = 0
i = 0 
while i < 1000 :
	results[i] = craps.play()
	i = i +1

#Games won on first,second...20..20+ rolls

j = 0
while j < 1000 :
	if results[j] > 0 :
		if results[j] > 20 :
			gamesWon[20] = gamesWon[20] + 1
		else :
			gamesWon[results[j]-1] = gamesWon[results[j]-1] + 1
	j = j + 1
#Games lost on first,second...20..20+ rolls
j = 0
while j < 1000 :
	if results[j] < 0 :
		if results[j] < -20 :
			gamesLost[20] = gamesLost[20] + 1
		else :
			gamesLost[-1*results[j]-1] = gamesLost[-1*results[j]-1] + 1
	j = j + 1
#Probability of winning among 1000 games
totalWins = 0 
for games in gamesWon :
	totalWins = totalWins + games
probWin = float(float(totalWins) / 1000.00)
#Average number of rolls on a game
totalRolls = 0
for rolls in results :
	if rolls < 0 :
		totalRolls = totalRolls + (rolls*-1)
	else :
		totalRolls = totalRolls + rolls
avgRolls = float(totalRolls/1000.00)
#print results
print 'Games won in 1,2,3...20,20+ rolls: \n', gamesWon
print 'Games lost in 1,2,3...20,20+ rolls: \n', gamesLost
print 'Prob. of Winning in 1000 games: ', probWin
print 'Average number of rolls among 1000 games', avgRolls
#write results
fileP = open('results.txt','wa')
fileP.write('Games won in 1,2,3...20,20+ rolls: \n {}\n'.format(gamesWon))
fileP.write('Games lost in 1,2,3...20,20+ rolls: \n {}\n'.format(gamesLost))
fileP.write('Prob. of Winning in 1000 games: {}\n'.format(probWin))
fileP.write('Average number of rolls among 1000 games {}\n'.format(avgRolls))
fileP.close()

