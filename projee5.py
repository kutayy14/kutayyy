def polybius_decrypt(ciphertext, key):
    # Polybius karesini oluştur
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    square = ''
    for char in key.upper():
        if char not in square and char in alphabet:
            square += char
    for char in alphabet:
        if char not in square:
            square += char

    # Şifrelenmiş metni çöz
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        if ciphertext[i].isalpha():
            row = int(ciphertext[i+1]) - 1
            col = int(ciphertext[i+2]) - 1
            plaintext += square[row*5 + col]
            i += 3
        else:
            plaintext += ciphertext[i]
            i += 1

    return plaintext

# Kullanıcıdan şifrelenmiş metin ve anahtar kelimeyi al
ciphertext = input("Şifrelenmiş metni girin: ")
key = input("Polybius karesinde kullanılacak anahtar kelimeyi girin: ")

# Şifre çözme işlemini gerçekleştir ve çözülmüş metni yazdır
plaintext = polybius_decrypt(ciphertext, key)
print("Çözülmüş Metin: " + plaintext)
