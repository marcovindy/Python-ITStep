# Program pro analýzu textových souborů:
# Vytvořte program, který bude schopen načíst textový soubor a provést na 
# něm následující analýzy:

# Vypsání celkového počtu slov v textu.
# Vypsání počtu unikátních slov v textu.
# Vypsání frekvence výskytu každého slova v textu, tedy počtu jeho výskytů.
# Vypsání pěti nejčastějších slov v textu.
# Program by měl být schopen pracovat s textovými soubory různých formátů a 
# měl by být ošetřen proti nevalidním vstupům.
































def analyze_text(file_path):
    # načtení souboru
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except IOError:
        print("Chyba při načítání souboru!")
        return

    # tokenizace textu
    words = text.split()

    # celkový počet slov
    total_words = len(words)
    print("Celkový počet slov:", total_words)

    # počet unikátních slov
    unique_words = set(words)
    num_unique_words = len(unique_words)
    print("Počet unikátních slov:", num_unique_words)

    # výpočet frekvence slov
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    # výpis frekvence slov
    print("Frekvence slov:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

    # výpis pěti nejčastějších slov
    print("Nejčastější slova:")
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    for word, freq in sorted_word_freq[:5]:
        print(f"{word}: {freq}")

analyze_text("cesta/k/souboru.txt")