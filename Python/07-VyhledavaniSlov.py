## Vyhledávání slov v textu:

# požádá uživatele o text a slovo, které chce vyhledat
text = input("Zadej text: ")
hledane_slovo = input("Zadej slovo, které chceš vyhledat: ")

# rozdělí text na slova a projde každé slovo, aby zjistil, zda obsahuje hledané slovo
nalezeno = False
for slovo in text.split():
    if slovo.lower() == hledane_slovo.lower():
        # pokud najde hledané slovo, vypíše jeho pozici a nastaví nalezeno na True
        pozice = text.index(slovo)
        print("Slovo '{}' nalezeno na pozici {}.".format(hledane_slovo, pozice))
        nalezeno = True

# pokud hledané slovo nebylo nalezeno, vypíše se zpráva o neúspěchu
if not nalezeno:
    print("Slovo '{}' nebylo nalezeno v textu.".format(hledane_slovo))
