def encrypt_rail_fence(plaintext, rails):
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    #print(fence)
    direction = 1
    row, col = 0, 0

    for char in plaintext:
        fence[row][col] = char
        col += 1

        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

        row += direction

    ciphertext = ''.join([''.join(row) for row in fence])
    return ciphertext

def decrypt_rail_fence(ciphertext, rails):
    # Initialize the fence matrix with empty spaces
    fence = [[' ' for _ in range(len(ciphertext))] for _ in range(rails)]

    # Fill the diagonals with '*'
    direction = 1
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        fence[row][col] = '*'
        col += 1

        # Change direction when reaching the top or bottom rail
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

        row += direction

    # Replace '*' with the ciphertext characters row-wise
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*' and index < len(ciphertext):
                fence[r][c] = ciphertext[index]
                index += 1

    # Reconstruct the plaintext reading diagonally
    plaintext = ''
    direction = 1
    row, col = 0, 0

    for _ in range(len(ciphertext)):
        plaintext += fence[row][col]
        col += 1

        # Change direction when reaching the top or bottom rail
        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

        row += direction

    return plaintext


# Example usage:
plaintext = "DEMONSLAYER"
rails = 3

print("Original text: ", plaintext)

encrypted_text = encrypt_rail_fence(plaintext, rails)
print(f"Encrypted: {encrypted_text}")

decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print(f"Decrypted: {decrypted_text}")