import os, json

# sets name to user input
name = input("Enter your name: ") 
# temporarily hardcoded
score = 5
scores_json = []

# reads the existing file and stores into scores_json
with open ("highScore.json", "r") as file:
    scores_json = json.load(file) 
    
# appends user input to current json data, writes back to json file
with open ("highScore.json", "w") as file:
    scores_json.append({
        "name": name,
        "score": score
    })
    json.dump(scores_json, file, indent=2, separators=(',',': '))