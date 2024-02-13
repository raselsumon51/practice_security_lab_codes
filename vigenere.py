def generateKey(plaintext,keyword):
    key =  list(keyword)
    # print(key)
    if len(plaintext)==len(key):
        return keyword
    else:
        for i in range(len(plaintext)-len(key)):
            key.append(key[i%len(key)])
    return "".join(key)

def cipherText(plaintext,key):
    res = []
    char =""
    for i in range(len(plaintext)):
        char = chr((ord(plaintext[i]) + ord(key[i]))%26 + ord('A'))
        res.append(char)
    return "".join(res)
def originalText(plaintext,key):
    res = []
    char =""
    for i in range(len(plaintext)):
        char = chr((ord(plaintext[i]) - ord(key[i]))%26 + ord('A'))
        res.append(char)
    return "".join(res)

plaintext = "SECRET MESSAGE"
keyword = "LEMON"
plaintext = plaintext.replace(" ","")
# print(plaintext)
key =  generateKey(plaintext,keyword)

cipherT = cipherText(plaintext,key)
print(f'Cipher text: {cipherT}')

originalT = originalText(cipherT,key)
print(f'Plain text: {originalT}')
