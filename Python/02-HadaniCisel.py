import random

# vygeneruje náhodné číslo od 1 do 100
nahodne_cislo = random.randint(1, 100)

# inicializuje proměnnou pro počet pokusů
pocet_pokusu = 0

# zahájí smyčku pro hádání čísla
while True:
    # požádá uživatele o tip na číslo
    tip = int(input("Zadej číslo od 1 do 100: "))
    pocet_pokusu += 1

    # porovná tip s náhodným číslem
    if tip == nahodne_cislo:
        print("Gratuluji, uhádl jsi číslo {} po {} pokusech.".format(nahodne_cislo, pocet_pokusu))
        break
    elif tip < nahodne_cislo:
        print("Tipni větší číslo.")
    else:
        print("Tipni menší číslo.")
