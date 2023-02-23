# požádá uživatele o zadání slova
word = input("Zadej slovo: ")

# porovná zadané slovo se slovem přečteným pozpátku a rozhodne, zda je slovo palindrom
if word == word[::-1]:
    print("Slovo je palindrom.")
else:
    print("Slovo není palindrom.")
