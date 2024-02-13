def generate_key(plainText,key):
    return key + plainText[:len(plainText)-len(autokey)]

def cipher_text(plainText,key):
    res = []
    char = ""
    for i in range(len(plainText)):
        char = chr((ord(plainText[i])+ ord(key[i]))%26 + ord('A'))
        res.append(char)
    return "".join(res)

def Original_text(cipher_text,key):
    res = []
    char = ""
    cipher_text_l = list(cipher_text)
    key_l = list(key)
    for i in range(len(cipher_text_l)):
        char = chr((ord(cipher_text_l[i])- ord(key_l[i]))%26 + ord('A'))
        res.append(char)
        key_l.append(char)
    return "".join(res)

plainText = "HELLO"
autokey = "N"
key = generate_key(plainText,autokey)

cipherT = cipher_text(plainText,key)
print(f'Cipher text is : {cipherT}')

plainT = Original_text(cipherT,autokey)
print(f'Plain text is : {plainT}')
