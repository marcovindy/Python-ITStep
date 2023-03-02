def calculator():
    # nacteni prikladu od uzivatele
    priklad = input("Zadej priklad (+, -, *, /): ")

    # rozdeleni prikladu na cisla a operaci
    slova = priklad.split()
    cisla = [float(s) for s in slova if s.isnumeric()]
    operace = [s for s in slova if s in ['+', '-', '*', '/']]

    # vypocet
    vysledek = cisla[0]
    for i in range(len(operace)):
        if operace[i] == '+':
            vysledek += cisla[i+1]
        elif operace[i] == '-':
            vysledek -= cisla[i+1]
        elif operace[i] == '*':
            vysledek *= cisla[i+1]
        elif operace[i] == '/':
            vysledek /= cisla[i+1]

    # vystup vysledku
    print("Vysledek je:", vysledek)

calculator()