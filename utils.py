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

def isLetterInWord(letter, word):
    return word.find(letter) != -1
#funkcja odsłania zgadnięte litery
#np. dla guess = ..e., word = pies i letter = p
# zwróci p.e.
def showLetterInWord(guess, word, letter):
    guess = list(guess)
    for i in range(0, len(guess)):
        if word[i] == letter:
            guess[i] = letter
    return "".join(guess)
