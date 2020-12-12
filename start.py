
def isWord(word):
    return word.isalpha()
def removeSpecialCharacters(word):
    return word.strip(".,<>?/"':;}]{[|\+=_-)0(9*8&7^6%5$4#3@2!1~`-*`)]}'"—")

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

# stats = {}
#
#
# file = open('quo-vadis.txt', 'r')
#
# for line in file:
#     line = line.strip()
#     if line != '':
#         words = line.split()
#         stats = updateStats(stats, words)
# file.close()
#
# stats10 = filterStatsByLength(stats, 19)
# print(stats10)
#

stats19 = {'niebezpieczeństwach': 1, 'prawdopodobniejszym': 2, 'niebezpieczeństwami': 1}

charStats = getCharStats(stats19)
print(charStats)

# {
#     'a': 3,
#     'b': 3,
#     'c': 2
#     itd
# }
