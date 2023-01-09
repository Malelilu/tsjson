import json
 #Öffne die Datei
with open('accounts.json', 'r') as f:
        # Lade die JSON-Daten aus der Datei
        data = json.load(f)

print(data)

for account in data:
 
     print("der Name ist:", account["name"])
 