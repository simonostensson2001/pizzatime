
vaken = "n"
print("du sover djupt som björnen i ide...") # vi ställer frågan 

while vaken == "n": #vi ger vaken nu värdet n 
    vaken = input("Vaknar du?[y/n]: ").lower() #nu fpr man 2 altenativ om man väljer n så loopas det och det börjar om men om man skriver y så går pogramet vidare.

print("du yeetar dig upp och springer in i duschen")

print("Någon har lämnat en brödrost i din dusch")

duscha = input("flyttar du på brödrosten?[y/n] ").lower()

if duscha == "n":
    exit("Kolla nu har du hämnat i helvetet du kanske inte skulle ha dushat med brödrosten")

elif duscha == "y":
    print("Du blir kliniskt ren och blir taggad för dagen")
else:
    print("DOES NOT COMPUTE")

season = False
while season == False:
    season = input("Vilken årstid är det? [Vinter,Vår,Sommar,Höst]").lower()
    if season == "Vår" or season == "Vinter" or season "Höst":
        print("Det är kallt och blöt utomhus")
        print("Du klär på dig vinterkläderna")
    elif season == "Sommar":
        print("Det är sommar och det är varmt och skönt")
    else:
        season = False