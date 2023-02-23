n = int(input("Zadej počet čísel, pro které chceš spočítat průměr: "))
cisla = []

# načtení čísel
for i in range(n):
    cislo = float(input(f"Zadej {i+1}. číslo: "))
    cisla.append(cislo)

# výpočet průměru
prumer = sum(cisla) / n

# výpis výsledku
print("Průměr zadaných čísel je:", prumer)
