currentwelt = "1"
w1 = "Welt 1"
w2 = "Welt 2"
w3 = "Welt 3"

bedingung = True
while bedingung : 
    land = input("In welcher Welt willst du reisen? Wähle zwischen 1-3: ")
    if land == "x":
        bedingung = False
    elif currentwelt == land:
        print("Kollege das geht nicht!!!!")
    elif land == "1":
        print("Du bist in", w1)
        currentwelt = land
    elif land == "2":
        print("Du bist in", w2)
        currentwelt = land
    elif land == "3":
        print("Du bist in", w3)
        