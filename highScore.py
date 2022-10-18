import os, json

name = input("Enter your name: ") 
score = 5
scores_json = []
dictionary = {
    "name": name,
    "score": score
}

# tempJson = json.dumps(dictionary, indent = 2)
# print(tempJson)
with open ("highScore.json", "r") as file:
    scores_json = json.load(file) 
    

with open ("highScore.json", "w") as file:
    scores_json.append({
        "name": name,
        "score": score
    })
    json.dump(scores_json, file, indent=2, separators=(',',': '))

print(scores_json)