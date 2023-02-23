# importuje knihovnu random pro generování náhodných čísel
import random

# požádá uživatele o délku posloupnosti a rozsah hodnot
length = int(input("Enter length of sequence: "))
min_num = int(input("Enter minimum value: "))
max_num = int(input("Enter maximum value: "))

# vygeneruje náhodnou posloupnost čísel v zadaném rozmezí
sequence = [random.randint(min_num, max_num) for _ in range(length)]

# vypíše vygenerovanou posloupnost
print("Generated sequence:", sequence)
