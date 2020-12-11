file = open('quo-vadis.txt', 'r')

lineNo = 0
for line in file:
    line = line.strip()
    lineNo += 1
    if line != '':
        print (f"{lineNo}: {line}")

file.close()
