import json

t = []

with open("cenz.txt", encoding="utf-8") as c:
    for i in c:
        word = i.lower().split("\n")[0]
        if word != "":
            t.append(word)

with open("cenz.json", "w", encoding="utf-8") as i:
    json.dump(t, i)