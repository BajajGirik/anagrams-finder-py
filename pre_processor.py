import json

sortedWordToWordsMap = {}

with open('static/dictionary.txt','r') as file:
    for line in file:
        for word in line.split():
            sortedWord = ''.join(sorted(word))

            if sortedWord in sortedWordToWordsMap:
                sortedWordToWordsMap[sortedWord] += f", {word}"
            else:
                sortedWordToWordsMap[sortedWord] = word

json.dump(sortedWordToWordsMap, open('static/meta.json', 'w'))
