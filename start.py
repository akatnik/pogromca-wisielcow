from utils import *

stats = {}

for file in readFilesFromDir('./book'):
    updateStatsFromFile(file, stats)

debug(f'Wczytano statystyki dla {len(stats)} wyrazów.')

guess = 'kompute.'
notGuessed = ''
guessed = guess.replace('.','') + notGuessed
wordLen = len(guess)

print(f'Wyraz ma {wordLen} liter')
filteredStats = filterStatsByLength(stats, wordLen)
filteredStats = filterStatsByGuessed(filteredStats, guess)
filteredStats = filterStatsByNotGuessed(filteredStats, notGuessed)

charStats = getCharStats(filteredStats)
debug(f'Statystyki liter: {charStats}')

char = selectChar(charStats, guessed)

print(char)
