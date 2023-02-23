## Heslo s omezeným počtem pokusů:

# nastaví správné heslo
SPRAVNE_HESLO = "tajneheslo"

# nastaví počet pokusů na 3
pocet_pokusu = 3

# zahájí smyčku pro zadávání hesla
while pocet_pokusu > 0:
    # požádá uživatele o zadání hesla
    zadane_heslo = input("Zadej heslo: ")
    pocet_pokusu -= 1

    # porovná zadané heslo se správným heslem
    if zadane_heslo == SPRAVNE_HESLO:
        print("Heslo bylo zadáno správně.")
        break
    else:
        print("Heslo bylo zadáno nesprávně. Zbývající počet pokusů:", pocet_pokusu)

if pocet_pokusu == 0:
    print("Byly vyčerpány všechny pokusy.")
