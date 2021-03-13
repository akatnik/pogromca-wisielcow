from utils import *
import sys

stats = {}

for file in readFilesFromDir('./book'):
    updateStatsFromFile(file, stats)

debug(f'Wczytano statystyki dla {len(stats)} wyrazów.')


# if (len(sys.argv) != 2):
#     print('Błąd! Podaj słowo jako argument programu')
#     exit(1)

# answer = sys.argv[1]
letersCount = input('podaj ilosc liter: ')


guess = '.' * int(letersCount)


notGuessed = ''
guessed = guess.replace('.','') + notGuessed
wordLen = len(guess)

print(f'Wyraz ma {wordLen} liter')

errorsCounter = 0
ok = False
while not ok and errorsCounter < 13:
    print('__________________________________________________')
    print(guess)
    filteredStats = filterStatsByLength(stats, wordLen)
    filteredStats = filterStatsByGuessed(filteredStats, guess)
    filteredStats = filterStatsByNotGuessed(filteredStats, notGuessed)

    charStats = getCharStats(filteredStats)
    debug(f'Statystyki liter: {charStats}')

    letter = selectChar(charStats, guessed)
    print(f"Kupuję literę {letter}")

    pos = askForLetter(letter)
    if len(pos) > 0 :
        guess = showLetterInWord(guess, pos, letter)
    else:
        print(f'Nie udało się')
        errorsCounter = errorsCounter + 1
    guessed = guessed + letter
    ok = guess.find('.') == -1
    if ok:
        print(f'słowo to "{guess}"')
print(f'Gra zakończona po {errorsCounter} błędach')
if (errorsCounter == 13):
    print(f'Przegrałem')
