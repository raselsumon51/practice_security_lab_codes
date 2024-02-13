def caesar_cipher(text, shift_amount):
    result = ""
    for char in text:
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            elif char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            else:
                shifted_char = char
            result = result + shifted_char
    return result

text = "ABC"
shift = 1
encrypted_text = caesar_cipher(text, shift)
print("Original text: ", text)
print("Encrypted text: ", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text: ", decrypted_text)
