## Šifrování pomocí Caesarovy šifry:

# požádá uživatele o zprávu a klíč pro šifrování
zprava = input("Zadej zprávu: ")
klic = int(input("Zadej klíč pro šifrování (celé číslo od 1 do 25): "))

# inicializuje prázdný řetězec pro uložení zakódované zprávy
zakodovana_zprava = ""

# projde všechna písmena zprávy a zakóduje je pomocí Caesarovy šifry
for pismeno in zprava:
    # ignoruje mezery a jiné znaky, které nejsou písmena
    if not pismeno.isalpha():
        zakodovana_zprava += pismeno
        continue
    # určuje index písmene v abecedě
    index_v_abecede = ord(pismeno.lower()) - 97
    # aplikuje posun pomocí klíče
    posunuty_index = (index_v_abecede + klic) % 26
    # přidá zakódované písmeno do řetězce
    zakodovane_pismeno = chr(posunuty_index + 97)
    zakodovana_zprava += zakodovane_pismeno.upper() if pismeno.isupper() else zakodovane_pismeno

# vypíše zakódovanou zprávu
print("Zakódovaná zpráva:", zakodovana_zprava)
