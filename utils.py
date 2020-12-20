from os import listdir
from os.path import isfile, join

def isMatching(guess, word):
    for i in range(0, len(guess)):
        if guess[i] != '.' and guess[i] != word[i]:
            return False
    return True

# Funkcja zwraca True jeżeli wyraz word nie zawiera ŻADNEJ lietry
# z tablicy letters
def doesntContain(word, letters):
    for letter in word:
        if letters.find(letter) >= 0:
            return False
    return True

    # jeżeli ta listera występuje w tablicy letters
    # to zwróć false
    # a jeżeli żadna litera nie wystpuje to zwróć True

def assertEquals(value, expectedValue):
    if (value == expectedValue):
        print('OK')
    else:
        print('ERROR')

# print('Testujemy funkcję isMatching')
# assertEquals(isMatching('....', 'pies'), True)
# assertEquals(isMatching('..e.', 'okno'), False)
# assertEquals(isMatching('..e.', 'okeo'), True)
# assertEquals(isMatching('..x.y', 'okxoy'), True)
# assertEquals(isMatching('..x.yz', 'okxoyf'), False)

# print('Testujemy funkcję doesntContain')
# assertEquals(doesntContain('kot', 'b'), True)
# assertEquals(doesntContain('kot', 'bo'), False)
# assertEquals(doesntContain('kot', 'ot'), False)
# assertEquals(doesntContain('kot', 'ab'), True)

def updateStatsFromFile(fileName, stats):
    file = open(fileName, 'r')

    for line in file:
        line = line.strip()
        if line != '':
            words = line.split()
            stats = updateStats(stats, words)
    file.close()

#Funkcja usuwa wszystkie znaki oprócz liter
def isWord(word):
    return word.isalpha()
def removeSpecialCharacters(word):
    return word.strip(".,<>?/"':;}]{[|\+=_-)0(9*8&7^6%5$4#3@2!1~`-*`)]}'"—")

#Funkcja namienia wszystkie litery na małe
def normalize(word):
    return word.lower()

def filterStatsByLength(stats, length):
    newStats = {}
    for key in stats.keys():
        if len(key) == length:
            newStats[key] = stats[key]
    return newStats

def updateStats(stats, words):
    for word in words:
        word = removeSpecialCharacters(word)
        word = normalize(word)
        if isWord(word):
            stats[word] = stats.get(word, 0) + 1
    return stats

def getCharStats(stats):
    charStats = {}
    for word in stats:
        for letter in word:
            charStats[letter] = charStats.get(letter, 0 ) + stats[word]
    return charStats

def selectChar(stats, guessed):
    letter = '-'
    max = 0
    for l in stats:
        if stats[l] > max and l not in guessed:
            max = stats[l]
            letter = l
    return letter

# Funkcja zwraca nowe statystyki wyrazów, takie, że wyrazy
# pasujące do wzorca guess, np:
# dla
#    stats = { 'ala': 2, 'ola': 5}
#    i guess = 'ol.'
# zwróci { 'ola': 5 }
def filterStatsByGuessed(stats, guess):
    filteredStats = {}
    for word in stats:
        if isMatching(guess,word):
            filteredStats[word] = stats[word]
    return filteredStats

# Funkcja zwraca nowe statystyki wyrazów, takie że wyrazy
# nie zaweierają liter z tablicy notPresent, np. dla:
#    stats = { 'ala': 2, 'ola': 5}
#    i notPrssent = ['o']
# zwróci { 'ala': 2 }
def filterStatsByNotGuessed(stats, notGuessed):
    filteredStats = {}
    for word in stats:
        if doesntContain(word, notGuessed):
            filteredStats[word] = stats[word]
# jeżeli nie zawiera żadnej litery z notGuessed
    return filteredStats

def debug(o):
  print(o)
  pass


def readFilesFromDir(dirName):
    files = []
    for f in listdir(dirName):
        fullPath = dirName + '/' + f
        if isfile(fullPath):
            files.append(fullPath)
    return files
