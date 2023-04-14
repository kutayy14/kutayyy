# Polybius şifreleme algoritması kullanarak metni şifreleme
def polybius(text):
    polybius_square = {'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
                      'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '24',
                      'k': '25', 'l': '31', 'm': '32', 'n': '33', 'o': '34',
                      'p': '35', 'q': '41', 'r': '42', 's': '43', 't': '44',
                      'u': '45', 'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55'}

    encrypted_text = ""
    for char in text.lower():
        if char in polybius_square:
            encrypted_text += polybius_square[char]
        elif char == " ":
            encrypted_text += " "
    return encrypted_text

# Kullanıcı adı girdisi al
name = input("Adınızı girin: ")

# Adı şifrele
encrypted_name = polybius(name)

# Sonucu ekrana yazdır
print("Şifrelenmiş adınız: " + encrypted_name)
