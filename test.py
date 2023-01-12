import json
 #Öffne die Datei
with open('accounts.json', 'r') as filejson:
        # Lade die JSON-Daten aus der Datei
        data = json.load(filejson)

eingabe = input('was moechtes du eingeben?\noption a: alter\noption b: kontostand\n')

if eingabe == "alter":
 for account in data:
        if int(account["age"]) >25:
               print("alter:", account["age"], "name:", account["name"])

# Höchsten Kontostand
if eingabe == "kontostand":
    summe = 0
    for accounts in data:
        pruf = accounts["balance"].replace(",","")
        pruf = float(pruf)
        if summe < pruf:
                summe = pruf
    print(summe)
