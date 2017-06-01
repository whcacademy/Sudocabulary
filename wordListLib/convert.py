# script to convert wordList.csv to .vocab bash list

import csv

wordArray = []
meaningArray = []
with open('wordList.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        wordArray.append(row[0])
        meaningArray.append(row[1])

wordArrayPrint = list(map(lambda x: "'" + x + "'", wordArray))
meaningArrayPrint =list(map(lambda x: '"' + x + '"', meaningArray))
print(wordArrayPrint[1000])
print(meaningArrayPrint[1000])
print('wordarray=( ' + ' '.join(wordArrayPrint) + ' )')
print('meaningarray=( ' + ' '.join(meaningArrayPrint) + ' )')