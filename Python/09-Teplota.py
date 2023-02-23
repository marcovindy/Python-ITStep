## Převod teploty mezi stupni Celsia a Fahrenheita:

# požádá uživatele o zadání teploty a jednotky
teplota = float(input("Zadej teplotu: "))
jednotka = input("Zadej jednotku teploty (C pro stupně Celsia, F pro stupně Fahrenheita): ")

# provede převod mezi stupni Celsia a Fahrenheita
if jednotka == "C":
    teplota_fahrenheita = teplota * 1.8 + 32
    print("Teplota v stupních Fahrenheita je:", teplota_fahrenheita)
elif jednotka == "F":
    teplota_celsia = (teplota - 32) / 1.8
    print("Teplota v stupních Celsia je:", teplota_celsia)
else:
    print("Neplatná jednotka teploty.")
