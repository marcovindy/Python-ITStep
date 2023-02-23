# požádá uživatele o zadání věty
veta = input("Zadej větu: ")

# rozdělí větu na slova a uloží do seznamu
slova = veta.split()

# seřadí slova podle abecedy a vytiskne
slova.sort()
print("Seřazená věta:", " ".join(slova))
