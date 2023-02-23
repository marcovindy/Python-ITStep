# požádá uživatele o dvě čísla a operaci, kterou chce provést
cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))
operace = input("Zadej operaci (+, -, *, /): ")

# provede operaci a vypíše výsledek
if operace == "+":
    vysledek = cislo1 + cislo2
elif operace == "-":
    vysledek = cislo1 - cislo2
elif operace == "*":
    vysledek = cislo1 * cislo2
elif operace == "/":
    vysledek = cislo1 / cislo2
else:
    print("Neplatná operace")
    exit()

print("Výsledek:", vysledek)
