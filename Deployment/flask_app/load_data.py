from pymongo import MongoClient
import json

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://root:password@localhost:27017/')
db = client['tactic']

# Charger les données du fichier tactic.json
with open('sub-technique.json', 'r') as file:
    data = json.load(file)
    for document in data:
        db.sub_techniques.insert_one(document)

# Fermeture de la connexion
client.close()
