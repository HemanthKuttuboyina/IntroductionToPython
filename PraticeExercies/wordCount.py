wordsDict = {}

with open("./text.txt", encoding="utf=8") as file:
    for line in file:
        line = line.lower()
        for p in ".?!/,":
            line = line.replace(p,"")
        for word in line.split():
            wordsDict[word] = wordsDict.get(word,0)+1
# print(wordsDict)
countOfUnique = 0
for word in wordsDict:
    if wordsDict.get(word) == 1:
        countOfUnique +=1
words = sorted(wordsDict)
print(f"Total words : {len(words)}")
print(f"Unique :{countOfUnique}")
# print(wordsDict)
for word in words:
    print(f"{word} : {wordsDict[word]}")
# print(line)