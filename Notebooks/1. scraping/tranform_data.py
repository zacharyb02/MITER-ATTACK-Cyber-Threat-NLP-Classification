import json

with open('tactic.json', 'r') as f:
    tactics = json.load(f)

techniques = []

for tactic in tactics :
    techniques