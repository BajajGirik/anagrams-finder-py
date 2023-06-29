import json

sortedWordToWords = json.load(open("static/meta.json"))

inp = input("Enter the word you want to search anagrams for: ")

sortedInp = "".join(sorted(inp))

if sortedInp in sortedWordToWords:
    print(sortedWordToWords[sortedInp])
else:
    print("No anagrams found")
