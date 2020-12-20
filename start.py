from utils import *
import sys

stats = {}

for file in readFilesFromDir('./book'):
    updateStatsFromFile(file, stats)

debug(f'Wczytano statystyki dla {len(stats)} wyrazów.')


if (len(sys.argv) != 2):
    print('Błąd! Podaj słowo jako argument programu')
    exit(1)

answer = sys.argv[1]
guess = '.' * len(answer)


notGuessed = ''
guessed = guess.replace('.','') + notGuessed
wordLen = len(guess)

print(f'Wyraz ma {wordLen} liter')

errorsCounter = 0
while guess != answer and errorsCounter < 13:
    print('__________________________________________________')
    print(guess)
    filteredStats = filterStatsByLength(stats, wordLen)
    filteredStats = filterStatsByGuessed(filteredStats, guess)
    filteredStats = filterStatsByNotGuessed(filteredStats, notGuessed)

    charStats = getCharStats(filteredStats)
    debug(f'Statystyki liter: {charStats}')

    letter = selectChar(charStats, guessed)
    print(f"Kupuję literę {letter}")

    if isLetterInWord(letter, answer):
        guess = showLetterInWord(guess, answer, letter)
        print(f'Brawo, litera {letter} została odsłonięta')
    else:
        print(f'Nie udało się')
        errorsCounter = errorsCounter + 1
    guessed = guessed + letter

print(f'Gra zakończona po {errorsCounter} błędach')
if (errorsCounter == 13):
    print(f'Przegrałeś, szukane słowo to {answer}')
