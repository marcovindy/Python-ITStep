abeceda = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(text, shift):
    # převede všechna písmena na malá
    text = text.lower()
    encrypted_text = ""
    for char in text:
        # přeskočí mezery a neznámé znaky
        if char not in abeceda:
            encrypted_text += char
            continue
        # aplikuje Caesarovu šifru na písmeno
        index = abeceda.index(char)
        shifted_index = (index + shift) % len(abeceda)
        encrypted_text += abeceda[shifted_index]
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    # převede všechna písmena na malá
    encrypted_text = encrypted_text.lower()
    text = ""
    for char in encrypted_text:
        # přeskočí mezery a neznámé znaky
        if char not in abeceda:
            text += char
            continue
        # aplikuje Caesarovu šifru na písmeno
        index = abeceda.index(char)
        shifted_index = (index - shift) % len(abeceda)
        text += abeceda[shifted_index]
    return text

# použití funkce pro šifrování textu
text = "Toto je tajný text."
shift = 3
encrypted_text = caesar_encrypt(text, shift)
print("Zašifrovaný text:", encrypted_text)

# použití funkce pro dešifrování textu
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Dešifrovaný text:", decrypted_text)
